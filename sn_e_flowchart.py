"""
Substitution & Elimination Reaction Flowchart
──────────────────────────────────────────────
Generates a decision flowchart for determining SN1, SN2, E1, or E2
reaction mechanisms based on substrate degree and reaction conditions.

Requirements:
    pip install graphviz
    Also needs Graphviz system package:
        macOS:   brew install graphviz
        Ubuntu:  sudo apt install graphviz
        Windows: choco install graphviz

Usage:
    python sn_e_flowchart.py
    → produces sn_e_flowchart.png and sn_e_flowchart.pdf
"""

import graphviz

def create_flowchart():
    dot = graphviz.Digraph(
        "SN_E_Flowchart",
        format="png",
        engine="dot",
    )

    # ── Global styling ──────────────────────────────────────────────
    dot.attr(
        rankdir="TB",
        bgcolor="#0d1117",
        fontname="Helvetica Neue",
        pad="0.8",
        nodesep="0.6",
        ranksep="0.7",
        label="Substitution & Elimination — Decision Flowchart\n\n",
        labelloc="t",
        fontsize="22",
        fontcolor="#e6edf3",
    )

    # ── Node style presets ──────────────────────────────────────────
    start_style = dict(
        shape="box", style="rounded,filled", fillcolor="#1a1f2e",
        color="#58a6ff", fontcolor="#58a6ff", fontname="Helvetica Neue Bold",
        fontsize="14", penwidth="2.5",
    )
    question_style = dict(
        shape="diamond", style="filled", fillcolor="#161b22",
        color="#f0883e", fontcolor="#f0883e", fontname="Courier Bold",
        fontsize="11", penwidth="2",
    )
    sn2_style = dict(
        shape="box", style="rounded,filled,bold", fillcolor="#0d4429",
        color="#3fb950", fontcolor="#3fb950", fontname="Helvetica Neue Bold",
        fontsize="14", penwidth="2.5",
    )
    sn1_style = dict(
        shape="box", style="rounded,filled,bold", fillcolor="#1a3a1a",
        color="#56d364", fontcolor="#56d364", fontname="Helvetica Neue Bold",
        fontsize="14", penwidth="2.5",
    )
    e2_style = dict(
        shape="box", style="rounded,filled,bold", fillcolor="#3d1f00",
        color="#f78166", fontcolor="#f78166", fontname="Helvetica Neue Bold",
        fontsize="14", penwidth="2.5",
    )
    e1_style = dict(
        shape="box", style="rounded,filled,bold", fillcolor="#3b1d00",
        color="#d29922", fontcolor="#d29922", fontname="Helvetica Neue Bold",
        fontsize="14", penwidth="2.5",
    )
    note_style = dict(
        shape="plaintext", fontcolor="#586069",
        fontname="Courier", fontsize="9",
    )

    # ── Edge style presets ──────────────────────────────────────────
    default_edge = dict(color="#30363d", fontcolor="#8b949e",
                        fontname="Courier Bold", fontsize="10", penwidth="1.8")
    yes_edge = dict(color="#3fb950", fontcolor="#3fb950",
                    fontname="Courier Bold", fontsize="10", penwidth="1.8")
    no_edge = dict(color="#f85149", fontcolor="#f85149",
                   fontname="Courier Bold", fontsize="10", penwidth="1.8")

    # ═══════════════════════════════════════════════════════════════
    #  NODES
    # ═══════════════════════════════════════════════════════════════

    # Start
    dot.node("start", "Substrate Carbon Degree?", **start_style)

    # ── 0° branch ──
    dot.node("sn2_0", "SN2", **sn2_style)

    # ── 1° branch ──
    dot.node("bulky_1", "Bulky\nbase?", **question_style)
    dot.node("e2_1", "E2", **e2_style)
    dot.node("sn2_1", "SN2", **sn2_style)
    dot.node("note_1", "(most of the time)", **note_style)

    # ── 2° branch ──
    dot.node("charge_2", "Nu⁻ has\ncharge?", **question_style)
    # YES → strong base?
    dot.node("strong_2", "Strong\nbase?", **question_style)
    dot.node("e2_2a", "E2", **e2_style)
    dot.node("sn2_2", "SN2", **sn2_style)
    # NO → heat?
    dot.node("heat_2", "Heat?", **question_style)
    dot.node("e1_2", "E1", **e1_style)
    dot.node("sn1_2", "SN1", **sn1_style)

    # ── 3° branch ──
    dot.node("strong_3", "Strong\nbase?", **question_style)
    dot.node("e2_3", "E2", **e2_style)
    dot.node("heat_3", "Heat?", **question_style)
    dot.node("e1_3", "E1", **e1_style)
    dot.node("sn1_3", "SN1", **sn1_style)

    # ═══════════════════════════════════════════════════════════════
    #  EDGES
    # ═══════════════════════════════════════════════════════════════

    # From start to each degree
    dot.edge("start", "sn2_0", label="  0°  ", **default_edge)
    dot.edge("start", "bulky_1", label="  1°  ", **default_edge)
    dot.edge("start", "charge_2", label="  2°  ", **default_edge)
    dot.edge("start", "strong_3", label="  3°  ", **default_edge)

    # ── 1° ──
    dot.edge("bulky_1", "e2_1", label=" YES ", **yes_edge)
    dot.edge("bulky_1", "sn2_1", label=" NO ", **no_edge)
    dot.edge("sn2_1", "note_1", style="invis")

    # ── 2° charged ──
    dot.edge("charge_2", "strong_2", label=" YES ", **yes_edge)
    dot.edge("strong_2", "e2_2a", label=" YES ", **yes_edge)
    dot.edge("strong_2", "sn2_2", label=" NO ", **no_edge)

    # ── 2° uncharged ──
    dot.edge("charge_2", "heat_2", label=" NO ", **no_edge)
    dot.edge("heat_2", "e1_2", label=" YES ", **yes_edge)
    dot.edge("heat_2", "sn1_2", label=" NO ", **no_edge)

    # ── 3° ──
    dot.edge("strong_3", "e2_3", label=" YES ", **yes_edge)
    dot.edge("strong_3", "heat_3", label=" NO ", **no_edge)
    dot.edge("heat_3", "e1_3", label=" YES ", **yes_edge)
    dot.edge("heat_3", "sn1_3", label=" NO ", **no_edge)

    return dot


if __name__ == "__main__":
    chart = create_flowchart()

    # Render PNG and PDF
    chart.render("sn_e_flowchart", cleanup=True)
    chart.format = "pdf"
    chart.render("sn_e_flowchart", cleanup=True)

    print("✓ Generated: sn_e_flowchart.png")
    print("✓ Generated: sn_e_flowchart.pdf")
