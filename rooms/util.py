import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def get_tenant_ids(tenant1, tenant2, tenant3):
    tenant_ids = []
    for tenant in [tenant1, tenant2, tenant3]:
        try:
            if tenant:
                tenant_ids.append(int(tenant))
        except ValueError:
            st.error(f"The tenant identifier '{tenant}' is not a valid number.")
            tenant_ids = []
            break

    return tenant_ids


def generate_compatibility_chart(compatibility):
    compatibility = compatibility / 100

    fig, ax = plt.subplots(figsize=(5, 4), facecolor="#323232")
    ax.set_facecolor("#323232")

    sns.barplot(
        x=compatibility.index,
        y=compatibility.values,
        ax=ax,
        color="white",
        edgecolor=None,
    )

    sns.despine(top=True, right=True, left=True, bottom=False)

    ax.set_xlabel("Tenant ID", fontsize=10, color="white")
    ax.set_ylabel("Similarity (%)", fontsize=10, color="white")

    xticks = ax.get_xticks()
    ax.set_xticks(xticks)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color="white")

    yticks = ax.get_yticks()
    ax.set_yticks(yticks)
    ax.set_yticklabels(
        ["{:.1f}%".format(y * 100) for y in ax.get_yticks()], fontsize=8, color="white"
    )

    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            "{:.1f}%".format(height * 100),
            (p.get_x() + p.get_width() / 2.0, height),
            ha="center",
            va="center",
            xytext=(0, 5),
            textcoords="offset points",
            fontsize=8,
            color="white",
        )

    return fig


def generate_compatibility_table(result):
    result_0_with_index = result[0].reset_index()
    result_0_with_index.rename(columns={"index": "Attribute"}, inplace=True)

    fig_table = go.Figure(
        data=[
            go.Table(
                columnwidth=[20] + [10] * (len(result_0_with_index.columns) - 1),
                header=dict(
                    values=list(result_0_with_index.columns),
                    fill_color="rgb(50, 50, 50)",
                    align="left",
                    font=dict(color="white"),
                ),
                cells=dict(
                    values=[
                        result_0_with_index[col] for col in result_0_with_index.columns
                    ],
                    fill_color="rgb(40, 40, 40)",
                    align="left",
                    font=dict(color="white"),
                ),
            )
        ]
    )

    fig_table.update_layout(
        width=700,
        height=320,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    return fig_table
