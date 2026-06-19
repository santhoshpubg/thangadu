# --- EMERGENCY RUNTIME TYPE PATCH ---
import builtins
import typing
builtins.Any = typing.Any 
# ------------------------------------

from fasthtml.common import *
from starlette.responses import Response, HTMLResponse
from supabase import create_client, Client

_app, _rt = fast_app(secret_key="some_long_secure_random_string_here_for_your_family_tree_session")

app = _app
rt = _rt
application = _app

family_data = [
    {"id": 1, "gen": 1, "name": "Songattae Joghee", "parent": None},
    {"id": 2, "gen": 2, "name": "Songattae Linga", "parent": 1},
    {"id": 3, "gen": 3, "name": "Madhayya", "parent": 2},
    {"id": 4, "gen": 3, "name": "Raman", "parent": 2},
    {"id": 5, "gen": 3, "name": "Lakshmanan", "parent": 2},
    {"id": 6, "gen": 3, "name": "Joghee", "parent": 2},
    {"id": 7, "gen": 4, "name": "Krishnan", "parent": 3},
    {"id": 8, "gen": 4, "name": "Lingan", "parent": 3},
    {"id": 9, "gen": 5, "name": "Maharajan", "parent": 7},
    {"id": 10, "gen": 5, "name": "Gopalan", "parent": 7},
    {"id": 11, "gen": 5, "name": "Sundaran", "parent": 7},
    {"id": 12, "gen": 5, "name": "Mohan", "parent": 7},
    {"id": 13, "gen": 6, "name": "Balasubramanian", "parent": 9},
    {"id": 14, "gen": 7, "name": "Dhakshinamoorthy", "parent": 13},
    {"id": 15, "gen": 8, "name": "Dhakshara", "parent": 14},
    {"id": 16, "gen": 7, "name": "Lingeshwaran", "parent": 13},
    {"id": 17, "gen": 6, "name": "Gowtham Ganesh", "parent": 10},
    {"id": 18, "gen": 7, "name": "Dev Adhitya", "parent": 17},
    {"id": 19, "gen": 6, "name": "Santhosh", "parent": 11},
    {"id": 20, "gen": 7, "name": "Deendayal", "parent": 19},
    {"id": 21, "gen": 5, "name": "Arumugan", "parent": 8},
    {"id": 22, "gen": 5, "name": "Chandran", "parent": 8},
    {"id": 23, "gen": 5, "name": "Sankaran", "parent": 8},
    {"id": 24, "gen": 5, "name": "Raman", "parent": 8},
    {"id": 25, "gen": 6, "name": "Kannan", "parent": 21},
    {"id": 26, "gen": 7, "name": "Jithendhar", "parent": 25},
    {"id": 27, "gen": 6, "name": "Suresh", "parent": 21},
    {"id": 28, "gen": 7, "name": "Sourath", "parent": 27},
    {"id": 29, "gen": 7, "name": "Amarnath", "parent": 27},
    {"id": 30, "gen": 6, "name": "Ramesh", "parent": 21},
    {"id": 31, "gen": 7, "name": "Abhilash", "parent": 30},
    {"id": 32, "gen": 6, "name": "Mani", "parent": 22},
    {"id": 33, "gen": 6, "name": "Vijayakumar", "parent": 23},
    {"id": 34, "gen": 6, "name": "Saravanan", "parent": 24},
    {"id": 35, "gen": 4, "name": "Subramani a.k.a Sivayya", "parent": 5},
    {"id": 36, "gen": 5, "name": "Bhojan", "parent": 35},
    {"id": 37, "gen": 6, "name": "Rubesh", "parent": 36},
    {"id": 38, "gen": 6, "name": "Rajesh", "parent": 36},
    {"id": 39, "gen": 4, "name": "Raman", "parent": 6},
    {"id": 40, "gen": 4, "name": "Shanmugan", "parent": 6},
    {"id": 41, "gen": 5, "name": "Radhakrishnan", "parent": 39},
    {"id": 42, "gen": 5, "name": "Ravi", "parent": 39},
    {"id": 43, "gen": 6, "name": "Parshith", "parent": 41},
    {"id": 44, "gen": 6, "name": "Sailesh", "parent": 41},
    {"id": 45, "gen": 6, "name": "Kishore", "parent": 42},
    {"id": 46, "gen": 5, "name": "Senthil", "parent": 40},
    {"id": 47, "gen": 6, "name": "Siddhesh Joghee", "parent": 46}
]

SUPABASE_URL = "https://cyjitmzyfqmwsfbruqpf.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aml0bXp5ZnFtd3NmYnJ1cXBmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE4MDUwOTAsImV4cCI6MjA5NzM4MTA5MH0.sSHvidL9ZXMbTOdnNyoCpTHAy6x_QXOnIGPoypWkI80"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Shared Style Template Block
SHARED_CSS = """
:root { --primary: #1a365d; --accent: #2b6cb0; --spouse-color: #d63384; --daughters-color: #6b46c1; --border-color: #cbd5e0; }
body { font-family: system-ui, sans-serif; background: #f4f7f6; padding: 0; margin: 0; color: #2d3748; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px 15px; }
.nav-bar { display: flex; justify-content: center; gap: 20px; background: white; border-bottom: 1px solid #e2e8f0; padding: 15px; font-weight: 600; }
.nav-bar a { color: var(--primary); text-decoration: none; padding: 6px 12px; border-radius: 6px; }
.nav-bar a:hover { background: #f7fafc; color: var(--accent); }
.nav-bar a.active { background: var(--primary); color: white; }
.hero-header { background: var(--primary); color: white; padding: 30px 20px; border-radius: 12px; text-align: center; margin-bottom: 25px; }
.tree ul { margin-left: 10px; position: relative; list-style-type: none; padding-left: 0; }
.tree li { margin: 0; padding: 8px 0 8px 25px; position: relative; }
.tree li::before { content: ""; position: absolute; top: 0; left: 0; border-left: 2px solid var(--border-color); height: 100%; }
.tree li::after { content: ""; position: absolute; top: 22px; left: 0; border-top: 2px solid var(--border-color); width: 22px; }
.tree li:last-child::before { height: 22px; }
.node-box { display: inline-flex; align-items: center; flex-wrap: wrap; gap: 4px; background: #f8fafc; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 6px; cursor: pointer; transition: all 0.2s; }
.node-box:hover { background: #edf2f7; transform: scale(1.02); }
.gen-badge { font-size: 0.7rem; font-weight: 700; padding: 2px 6px; border-radius: 4px; background: #ebf8ff; color: #2b6cb0; }
.spouse-container { color: var(--spouse-color); font-weight: 500; }
.daughters-container { color: var(--daughters-color); font-weight: 400; font-style: italic; }
.heritage-table { width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 0.95rem; background: white; }
.heritage-table th { background: #f7fafc; color: #4a5568; text-align: left; padding: 12px; border: 1px solid #e2e8f0; font-weight: 600; }
.heritage-table td { padding: 12px; border: 1px solid #e2e8f0; vertical-align: top; color: #2d3748; }
input[type="text"] { width: 100%; padding: 10px; margin: 8px 0 16px 0; border: 1px solid #cbd5e0; border-radius: 6px; box-sizing: border-box; }
label { font-size: 0.9rem; font-weight: 600; color: #4a5568; }
button { padding: 10px 16px; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; }
button[type="submit"] { background: var(--accent); color: white; }
button.secondary { background: #e2e8f0; color: #4a5568; }
"""

def get_nav_bar(active_page):
    return Div(
        A("🌳 Family Lineage Tree", href="/", cls="active" if active_page == "tree" else ""),
        A("📜 Naming & Heritage Story", href="/heritage", cls="active" if active_page == "heritage" else ""),
        cls="nav-bar"
    )

def get_spouses_dict():
    try:
        response = supabase.table("family_spouses").select("*").execute()
        return {row["member_id"]: str(row["spouse_name"]) for row in response.data}
    except Exception:
        return {}

def get_daughters_dict():
    try:
        response = supabase.table("family_daughters").select("*").execute()
        d_map = {}
        for row in response.data:
            m_id = row["member_id"]
            if m_id not in d_map:
                d_map[m_id] = []
            d_map[m_id].append(str(row["daughter_name"]))
        return d_map
    except Exception:
        return {}

def generate_html_tree(parent_id, spouses, daughters):
    children = [m for m in family_data if m["parent"] == parent_id]
    if not children: 
        return []
    
    list_items = []
    for member in children:
        spouse_name = spouses.get(member["id"], "")
        member_daughters = daughters.get(member["id"], [])
        
        node_contents = [
            Span(f"Gen {member['gen']}", cls="gen-badge"),
            Span(str(member["name"]), style="font-weight:600;")
        ]
        if spouse_name:
            node_contents.append(Span(f" ❤️ {spouse_name}", cls="spouse-container"))
        
        if member_daughters:
            d_str = ", ".join(member_daughters)
            node_contents.append(Span(f" 👧 ({d_str})", cls="daughters-container"))
            
        node = Div(
            *node_contents,
            cls="node-box",
            hx_get=f"/edit-spouse-modal/{member['id']}",
            hx_target="#modal-placeholder"
        )
        
        sub_children_items = generate_html_tree(member["id"], spouses, daughters)
        if len(sub_children_items) > 0:
            list_items.append(Li(node, Ul(*sub_children_items)))
        else:
            list_items.append(Li(node))
            
    return list_items

# --- ROUTE 1: THE HOME TREE PAGE ---
@app.route("/")
async def get_homepage(request):
    spouses = get_spouses_dict()
    daughters = get_daughters_dict()
    tree_items = generate_html_tree(None, spouses, daughters)
    
    tree_container = Div("No family records loaded.", cls="tree") if len(tree_items) == 0 else Div(Ul(*tree_items), cls="tree")
        
    layout = Div(
        get_nav_bar("tree"),
        Div(
            Div(
                H1("Songattae Family of The Cool, Misty Forest Land Thangadu"),
                P("Interactive Family Lineage & Records (FastHTML Engine)"),
                cls="hero-header"
            ),
            Div(
                H2("🌳 Active Lineage Tree Chart", style="color: var(--primary); margin-top: 0; margin-bottom: 15px; font-size: 1.3rem; font-weight: 600;"),
                P("Click on any family node box to manage or append spouses and daughters dynamically.", style="color: #718096; font-size: 0.9rem; margin-bottom: 20px;"),
                tree_container,
                style="background: white; padding: 30px; border-radius: 12px; border: 1px solid #e2e8f0; overflow-x: auto; margin-bottom: 25px;"
            ),
            Div(id="modal-placeholder"),
            Footer(
                Hr(style="border: 0; border-top: 1px solid #cbd5e0; margin: 40px 0 20px 0;"),
                Div(
                    P("© 2026 Songattae Family. All Rights Reserved.", style="margin: 5px 0; font-weight: 500;"),
                    P("Contacts: contact@thangadu.family | Built with FastHTML & Supabase", style="margin: 5px 0; font-size: 0.9rem; color: #718096;"),
                    style="text-align: center; padding-bottom: 20px; color: #4a5568;"
                )
            ),
            cls="container"
        )
    )
    
    html_content = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>Thangadu Family Tree</title><script src='https://unpkg.com/htmx.org@1.9.12'></script><style>{SHARED_CSS}</style></head><body>{to_xml(layout)}</body></html>"
    return HTMLResponse(content=html_content, status_code=200)

# --- ROUTE 2: THE DEDICATED HERITAGE STORY PAGE ---
@app.route("/heritage")
async def get_heritage_page(request):
    layout = Div(
        get_nav_bar("heritage"),
        Div(
            Div(
                H1("Songattae Family Heritage & Origins"),
                P("Preserving the Naming Lineage Traditions of Thangadu"),
                cls="hero-header"
            ),
            Div(
                H2("📜 Origins & Naming Heritage", style="color: var(--primary); margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; font-size: 1.4rem;"),
                P("Rooted deeply in classic Badaga naming tradition, prefixes honor ancestral achievements. When a family elder achieved great respect, leadership, or performed an impactful community feat, their birth name was permanently prefixed with their village, agricultural estate, or monumental achievement."),
                P("As our foundational patriarch, ", B("Songattae Joghee"), " carries two beautiful historical possibilities passed down through generations:"),
                
                Ul(
                    Li(B("The Master of the Monsoon Waters: "), "As an early pioneer or elder (Gowda), he likely designed and constructed a vital stone check-dam ('Songattae') that channeled heavy monsoon water safely into valley farm plots, sustaining village crop yields during relentless misty downpours (Soan)."),
                    Li(B("The Leader from the Misty Ridge: "), "Alternatively, his clan was the very first to successfully clear and homestead that specific wet mountain ridge, establishing himself as the definitive guardian and elder patriarch of that slope."),
                    style="padding-left: 20px; margin-bottom: 25px;"
                ),
                
                H3("How to Read the Ancestor Prefix Block:", style="font-size: 1.1rem; color: #4a5568; margin-bottom: 10px;"),
                Table(
                    Tr(Th("Ancestor Name"), Th("Component Breakdown"), Th("Historical Insight")),
                    Tr(
                        Td(B("Songattae Joghee")),
                        Td(
                            Div(B("Songattae: "), "The Monsoon Embankment / Misty Ridge"),
                            Div(B("Joghee: "), "Revered Badaga baseline name (Yogi/Devotion)")
                        ),
                        Td("A foundational mountain patriarch celebrated for strategic water-management or initial land-holding along the high misty forest line of Thangadu.")
                    ),
                    cls="heritage-table"
                ),
                style="background: #ffffff; padding: 35px; border-radius: 12px; border: 1px solid #e2e8f0; line-height: 1.7; margin-bottom: 25px;"
            ),
            Footer(
                Hr(style="border: 0; border-top: 1px solid #cbd5e0; margin: 40px 0 20px 0;"),
                Div(
                    P("© 2026 Songattae Family. All Rights Reserved.", style="margin: 5px 0; font-weight: 500;"),
                    P("Contacts: contact@thangadu.family | Built with FastHTML & Supabase", style="margin: 5px 0; font-size: 0.9rem; color: #718096;"),
                    style="text-align: center; padding-bottom: 20px; color: #4a5568;"
                )
            ),
            cls="container"
        )
    )
    
    html_content = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>Family Heritage - Thangadu</title><style>{SHARED_CSS}</style></head><body>{to_xml(layout)}</body></html>"
    return HTMLResponse(content=html_content, status_code=200)

# --- CORE MODAL VIEWS & API ENDPOINTS ---
@app.route("/edit-spouse-modal/{member_id}")
async def get_modal_view(request):
    member_id = int(request.path_params["member_id"])
    member = next((m for m in family_data if m["id"] == member_id), None)
    
    spouses = get_spouses_dict()
    current_spouse = spouses.get(member_id, "")
    
    daughters = get_daughters_dict()
    current_daughters = ", ".join(daughters.get(member_id, []))
    
    modal_layout = Div(
        Div(
            H3(f"Manage Family for {str(member['name'])}"),
            Form(
                Label("Spouse Name"),
                Input(type="text", name="spouse_name", value=str(current_spouse), placeholder="Enter spouse's full name..."),
                
                Label("Daughters (Separate multiple names with commas)"),
                Input(type="text", name="daughters_list", value=str(current_daughters), placeholder="e.g. Dhakshara, Priya, Ananya"),
                
                Input(type="hidden", name="member_id", value=str(member_id)),
                Div(
                    Button("Cancel", type="button", onclick="document.getElementById('custom-modal').remove()", cls="secondary"),
                    Button("Save Updates", type="submit"),
                    style="display: flex; justify-content: flex-end; gap: 10px;"
                ),
                hx_post="/save-spouse"
            ),
            style="background: white; padding: 25px; border-radius: 10px; width: 90%; max-width: 450px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);"
        ),
        id="custom-modal",
        style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; justify-content: center; align-items: center; z-index: 1000;"
    )
    return HTMLResponse(content=to_xml(modal_layout), status_code=200)

@app.route("/save-spouse", methods=["POST"])
async def post_save_spouse(request):
    form_data = await request.form()
    member_id = int(form_data.get("member_id"))
    spouse_name = str(form_data.get("spouse_name", "")).strip()
    daughters_raw = str(form_data.get("daughters_list", "")).strip()
    
    if spouse_name:
        supabase.table("family_spouses").upsert({"member_id": member_id, "spouse_name": spouse_name}).execute()
    else:
        supabase.table("family_spouses").delete().eq("member_id", member_id).execute()
        
    supabase.table("family_daughters").delete().eq("member_id", member_id).execute()
    
    if daughters_raw:
        name_list = [n.strip() for n in daughters_raw.split(",") if n.strip()]
        if name_list:
            insert_rows = [{"member_id": member_id, "daughter_name": name} for name in name_list]
            supabase.table("family_daughters").insert(insert_rows).execute()
        
    response = Response(status_code=200)
    response.headers["HX-Refresh"] = "true"
    return response

if __name__ == "__main__":
    serve()
