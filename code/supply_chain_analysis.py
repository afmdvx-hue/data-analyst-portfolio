"""
Supply Chain Analytics
========================
Reproducible KPI pipeline for multi-channel retail supply data:
cost structure, supplier scorecards, logistics performance, and quality risk.

Dataset: Kaggle — harshsingh2209/supply-chain-analysis (CC0-1.0)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

CONFIG = {
    "data_path": "data/supply-chain/supply_chain_data.csv",
    "on_time_lead_days": 20,
    "defect_alert_pct": 3.0,
}


def load_data(path: str | Path | None = None) -> pd.DataFrame:
    root = Path(__file__).resolve().parents[2]
    p = Path(path) if path else root / CONFIG["data_path"]
    if not p.exists():
        raise FileNotFoundError(f"Dataset not found: {p}. Run: npm run fetch:supply-chain")
    return pd.read_csv(p)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [c.strip() for c in out.columns]
    numeric_cols = out.select_dtypes(include="number").columns
    for col in numeric_cols:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["SKU", "Revenue generated", "Costs"])
    out["margin_pct"] = (
        (out["Revenue generated"] - out["Costs"]) / out["Revenue generated"].replace(0, np.nan) * 100
    )
    out["unit_cost"] = out["Costs"] / out["Number of products sold"].replace(0, np.nan)
    out["on_time"] = out["Lead time"] <= CONFIG["on_time_lead_days"]
    out["quality_flag"] = out["Defect rates"] >= CONFIG["defect_alert_pct"]
    return out


def supplier_scorecard(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Supplier name", as_index=False)
        .agg(
            skus=("SKU", "count"),
            revenue=("Revenue generated", "sum"),
            avg_lead_time=("Lead time", "mean"),
            avg_defect_rate=("Defect rates", "mean"),
            on_time_pct=("on_time", "mean"),
            avg_shipping_cost=("Shipping costs", "mean"),
        )
        .assign(on_time_pct=lambda x: (x["on_time_pct"] * 100).round(1))
    )


def product_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Product type", as_index=False)
        .agg(
            skus=("SKU", "count"),
            units_sold=("Number of products sold", "sum"),
            revenue=("Revenue generated", "sum"),
            avg_price=("Price", "mean"),
            avg_defect=("Defect rates", "mean"),
            total_costs=("Costs", "sum"),
        )
        .sort_values("revenue", ascending=False)
    )


def logistics_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["Transportation modes", "Routes"], as_index=False)
        .agg(
            orders=("SKU", "count"),
            avg_shipping_time=("Shipping times", "mean"),
            avg_shipping_cost=("Shipping costs", "mean"),
            revenue=("Revenue generated", "sum"),
        )
    )


def compute_kpis(df: pd.DataFrame) -> dict[str, Any]:
    total_revenue = float(df["Revenue generated"].sum())
    total_costs = float(df["Costs"].sum())
    on_time_pct = float(df["on_time"].mean() * 100)
    avg_defect = float(df["Defect rates"].mean())
    quality_risk = int(df["quality_flag"].sum())
    top_product = (
        df.groupby("Product type")["Revenue generated"].sum().idxmax()
    )
    return {
        "rows": len(df),
        "total_revenue": round(total_revenue, 2),
        "total_costs": round(total_costs, 2),
        "margin_pct": round((total_revenue - total_costs) / total_revenue * 100, 1),
        "on_time_pct": round(on_time_pct, 1),
        "avg_defect_rate": round(avg_defect, 2),
        "quality_risk_skus": quality_risk,
        "top_product_type": top_product,
        "locations": int(df["Location"].nunique()),
        "suppliers": int(df["Supplier name"].nunique()),
    }


def run_pipeline(path: str | Path | None = None) -> dict[str, Any]:
    raw = load_data(path)
    data = clean_data(raw)
    return {
        "data": data,
        "kpis": compute_kpis(data),
        "suppliers": supplier_scorecard(data),
        "products": product_summary(data),
        "logistics": logistics_summary(data),
    }


if __name__ == "__main__":
    results = run_pipeline()
    print("Supply chain KPIs:")
    for k, v in results["kpis"].items():
        print(f"  {k}: {v}")
