# --- EMERGENCY RUNTIME TYPE PATCH ---
import builtins
import typing
builtins.Any = typing.Any 
# ------------------------------------

from fasthtml.common import *
from supabase import create_client, Client

# Add secret_key here to stop FastHTML from trying to write a file
_app, _rt = fast_app(
    secret_key="some_long_secure_random_string_here_for_your_family_tree_session",
    hdrs=(
        Script(src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"),
        Style("""
            :root { --primary: #1a365d; --accent: #2b6cb0; --spouse-color: #d63384; --border-color: #cbd5e0; }
            body { font-family: system-ui, sans-serif; background: #f4f7f6; padding: 30px 15px; }
            .tree ul { margin-left: 10px; position: relative; list-style-type: none; padding-left: 0; }
            .tree li { margin: 0; padding: 8px 0 8px 25px; position: relative; }
            .tree li::before { content: ""; position: absolute; top: 0; left: 0; border-left: 2px solid var(--border-color); height: 100%; }
            .tree li::after { content: ""; position: absolute; top: 22px; left: 0; border-top: 2px solid var(--border-color); width: 22px; }
            .tree li:last-child::before { height: 22px; }
            .node-box { display: inline-flex; align-items: center; background: #f8fafc; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 6px; cursor: pointer; }
            .gen-badge { font-size: 0.7rem; font-weight: 700; padding: 2px 6px; border-radius: 4px; margin-right: 8px; background: #ebf8ff; color: #2b6cb0; }
            .spouse-container { color: var(--spouse-color); font-weight: 500; margin-left: 6px; }
        """)
    )
)

app = _app
rt = _rt
application = _app

# --- Family Dataset ---
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

def get_spouses_dict():
    try:
        response = supabase.table("family_spouses").select("*").execute()
        return {row["member_id"]: row["spouse_name"] for row in response.data}
    except Exception:
        return {}

def generate_html_tree(parent_id, spouses):
    children = [m for m in family_data if m["parent"] == parent_id]
    if not children: return ""
    list_items = []
    for member in children:
        spouse_name = spouses.get(member["id"], "")
        spouse_element = Span(f" ❤️ {spouse_name}", cls="spouse-container") if spouse_name else ""
        node = Div(
            Span(f"Gen {member['gen']}", cls="gen-badge"),
            Span(member["name"], style="font-weight:600;"),
            spouse_element,
            cls="node-box",
            hx_get=f"/edit-spouse-modal/{member['id']}",
            hx_target="#modal-placeholder"
        )
        sub_tree = generate_html_tree(member["id"], spouses)
        
        # FIXED: Only wrap with NotStr if there is actual HTML layout string content
        if sub_tree:
            list_items.append(Li(node, NotStr(sub_tree)))
        else:
            list_items.append(Li(node))
            
    return f"<ul>{''.join([str(item) for item in list_items])}</ul>"

@rt("/")
def get():
    spouses = get_spouses_dict()
    tree_content = generate_html_tree(None, spouses)
    return Container(
        Header(
            H1("Songattae Family of The Cool, Misty Forest Land Thangadu"),
            P("Interactive Family Lineage & Records (FastHTML Engine)"),
            style="background: var(--primary); color: white; padding: 25px; border-radius: 12px; text-align: center; margin-bottom: 25px;"
        ),
        Div(
            Div(NotStr(tree_content), cls="tree"),
            style="background: white; padding: 30px; border-radius: 12px; border: 1px solid #e2e8f0; overflow-x: auto;"
        ),
        Div(id="modal-placeholder")
    )

@rt("/edit-spouse-modal/{member_id}")
def get_modal(member_id: int):
    member = next((m for m in family_data if m["id"] == member_id), None)
    spouses = get_spouses_dict()
    current_spouse = spouses.get(member_id, "")
    return Div(
        Div(
            H3(f"Update Spouse for {member['name']}"),
            Form(
                Input(type="text", name="spouse_name", value=current_spouse, placeholder="Enter full name"),
                Input(type="hidden", name="member_id", value=member_id),
                Div(
                    Button("Cancel", type="button", onclick="document.getElementById('custom-modal').remove()", cls="secondary"),
                    Button("Save Changes", type="submit"),
                    style="display: flex; justify-content: flex-end; gap: 10px;"
                ),
                hx_post="/save-spouse",
                hx_target="body"
            ),
            style="background: white; padding: 25px; border-radius: 10px; width: 90%; max-width: 400px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);"
        ),
        id="custom-modal",
        style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; justify-content: center; align-items: center; z-index: 1000;"
    )

@rt("/save-spouse")
def post(member_id: int, spouse_name: str):
    spouse_name = spouse_name.strip()
    if spouse_name:
        supabase.table("family_spouses").upsert({"member_id": member_id, "spouse_name": spouse_name}).execute()
    else:
        supabase.table("family_spouses").delete().eq("member_id", member_id).execute()
    return get()

# Only run server if called locally
if __name__ == "__main__":
    serve()
