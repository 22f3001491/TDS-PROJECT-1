from llm_generator import generate_app_code

brief = "Create a simple HTML page with 2 buttons: Login and Sign Up"
files = generate_app_code(brief)

print("Generated files:")
for fname, content in files["files"].items():
    print(f"--- {fname} ---\n{content[:500]}...\n")  # print first 500 chars
with open("test_index.html", "w", encoding="utf-8") as f:
    f.write(files["files"]["index.html"])
