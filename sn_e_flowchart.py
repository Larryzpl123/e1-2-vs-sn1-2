"""
Substitution & Elimination Reaction Flowchart
──────────────────────────────────────────────
Color coding:
    SN2 → Blue border      SN1 → Green border
    E2  → Dark red border   E1 → Yellow/gold border

Requirements:
    pip install graphviz
    System: brew install graphviz / sudo apt install graphviz

Usage:
    python sn_e_flowchart.py
"""

import graphviz

def create_flowchart():
    dot = graphviz.Digraph("SN_E_Flowchart", format="png", engine="dot")

    dot.attr(
        rankdir="TB", bgcolor="white", fontname="Helvetica Neue",
        pad="0.8", nodesep="0.6", ranksep="0.7",
        label="Substitution & Elimination — Decision Flowchart\n\n",
        labelloc="t", fontsize="22", fontcolor="#1a1a1a", dpi="200",
    )

    # Colors
    blue, green, dark_red, gold = "#2563eb", "#16a34a", "#b91c1c", "#ca8a04"
    slate = "#334155"

    # Style presets
    start   = dict(shape="box", style="rounded,filled,bold", fillcolor="#f1f5f9",
                   color=slate, fontcolor=slate, fontname="Helvetica Neue Bold",
                   fontsize="14", penwidth="2.5")
    quest   = dict(shape="diamond", style="filled", fillcolor="#f8f9fa",
                   color="#6b7280", fontcolor="#374151", fontname="Helvetica Neue Bold",
                   fontsize="11", penwidth="2")
    sn2     = dict(shape="box", style="rounded,filled,bold", fillcolor="#eff6ff",
                   color=blue, fontcolor=blue, fontname="Helvetica Neue Bold",
                   fontsize="14", penwidth="3")
    sn1     = dict(shape="box", style="rounded,filled,bold", fillcolor="#f0fdf4",
                   color=green, fontcolor=green, fontname="Helvetica Neue Bold",
                   fontsize="14", penwidth="3")
    e2      = dict(shape="box", style="rounded,filled,bold", fillcolor="#fef2f2",
                   color=dark_red, fontcolor=dark_red, fontname="Helvetica Neue Bold",
                   fontsize="14", penwidth="3")
    e1      = dict(shape="box", style="rounded,filled,bold", fillcolor="#fefce8",
                   color=gold, fontcolor=gold, fontname="Helvetica Neue Bold",
                   fontsize="14", penwidth="3")
    note    = dict(shape="plaintext", fontcolor="#9ca3af", fontname="Helvetica Neue",
                   fontsize="9")

    edge_d  = dict(color="#94a3b8", fontcolor="#64748b", fontname="Helvetica Neue Bold",
                   fontsize="10", penwidth="1.8")
    edge_y  = dict(color="#16a34a", fontcolor="#16a34a", fontname="Helvetica Neue Bold",
                   fontsize="10", penwidth="1.8")
    edge_n  = dict(color="#dc2626", fontcolor="#dc2626", fontname="Helvetica Neue Bold",
                   fontsize="10", penwidth="1.8")

    # ── Nodes ──
    dot.node("start", "Substrate Carbon Degree?", **start)

    dot.node("sn2_0", "SN2", **sn2)

    dot.node("bulky_1", "Bulky\nbase?", **quest)
    dot.node("e2_1", "E2", **e2)
    dot.node("sn2_1", "SN2", **sn2)
    dot.node("note_1", "(most of the time)", **note)

    dot.node("charge_2", "Nu⁻ has\ncharge?", **quest)
    dot.node("strong_2", "Strong\nbase?", **quest)
    dot.node("e2_2a", "E2", **e2)
    dot.node("sn2_2", "SN2", **sn2)
    dot.node("heat_2", "Heat?", **quest)
    dot.node("e1_2", "E1", **e1)
    dot.node("sn1_2", "SN1", **sn1)

    dot.node("strong_3", "Strong\nbase?", **quest)
    dot.node("e2_3", "E2", **e2)
    dot.node("heat_3", "Heat?", **quest)
    dot.node("e1_3", "E1", **e1)
    dot.node("sn1_3", "SN1", **sn1)

    # ── Edges ──
    dot.edge("start", "sn2_0",   label="  0°  ", **edge_d)
    dot.edge("start", "bulky_1", label="  1°  ", **edge_d)
    dot.edge("start", "charge_2",label="  2°  ", **edge_d)
    dot.edge("start", "strong_3",label="  3°  ", **edge_d)

    dot.edge("bulky_1", "e2_1",  label=" YES ", **edge_y)
    dot.edge("bulky_1", "sn2_1", label=" NO ",  **edge_n)
    dot.edge("sn2_1", "note_1",  style="invis")

    dot.edge("charge_2", "strong_2", label=" YES ", **edge_y)
    dot.edge("strong_2", "e2_2a",    label=" YES ", **edge_y)
    dot.edge("strong_2", "sn2_2",    label=" NO ",  **edge_n)
    dot.edge("charge_2", "heat_2",   label=" NO ",  **edge_n)
    dot.edge("heat_2",   "e1_2",     label=" YES ", **edge_y)
    dot.edge("heat_2",   "sn1_2",    label=" NO ",  **edge_n)

    dot.edge("strong_3", "e2_3",  label=" YES ", **edge_y)
    dot.edge("strong_3", "heat_3",label=" NO ",  **edge_n)
    dot.edge("heat_3",   "e1_3",  label=" YES ", **edge_y)
    dot.edge("heat_3",   "sn1_3", label=" NO ",  **edge_n)

    return dot

if __name__ == "__main__":
    chart = create_flowchart()
    chart.render("sn_e_flowchart", cleanup=True)
    chart.format = "pdf"
    chart.render("sn_e_flowchart", cleanup=True)
    print("✓ Generated: sn_e_flowchart.png")
    print("✓ Generated: sn_e_flowchart.pdf")
