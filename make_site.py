import g4f

print("Connecting to AI... Generating Trixie's Premium Portfolio Website...")

detailed_prompt = """
Write a single-file, highly polished, fully responsive modern developer portfolio website using valid HTML5 and Tailwind CSS via its CDN link. 

Apply these explicit visual layout configurations:
- Visual Theme: Professional coding aesthetic with a gorgeous GRADIENT pastel blue background layout theme. 
- Styling Traits: Clean professional typography, balanced layout spacing, strategic tech-focused icon badges, subtle hover micro-interactions, no massive walls of text, no excessive emoji spam, and a crisp user experience structure optimized for a technical recruiter.

Incorporate this exact structural content:
1. HERO INTRO SECTION:
   - Primary Display Name: Trixie B. Alas-as
   - Headline Title: Fresh BSIT Graduate • Aspiring Software Engineer
   - Text Introduction: "Hi, I'm Trixie Alas-as, a second-year BSIT (Bachelor of Science in Information Technology) student. As I continue my college journey, I want to improve my knowledge and become more confident in using technology. I'm interested in learning different skills, especially through activities, projects, and hands-on experiences in school. I know that I still have a lot to learn, so I'm willing to listen to advice, learn from my mistakes, and keep improving. I'm looking forward to gaining more experience and developing the skills I need for my future career in Information Technology."
   - Explicit Tone Guideline: Keep it personal, genuine, and professional. Avoid stale corporate buzzword biographies.

2. CORE TECH STACK SECTION:
   - Header Section Title: "Technologies I have worked with"
   - Languages: C++, Java, PHP, HTML, CSS (Explicitly labeled as Beginner / Entry-Level skills).
   - Tools & Environment: Visual Studio, Visual Studio Code, Git, GitHub, Canva, Microsoft Office.

3. FEATURED WORK & PROJECTS GRID:
   - Include 3 distinct interactive layout cards linking to your local folders:
     * Card 1: AFTER_EXAM (Link destination button: ./AFTER_EXAM/index.html)
     * Card 2: NSTP (Link destination button: ./NSTP/index.html)
     * Card 3: VLOG (Link destination button: ./VLOG/index.html)
   - Include a primary anchor badge button linking directly to your main verified repository deployment: https://github.io

4. CURRENTLY LEARNING SECTION:
   - Display a list focusing on continuous skill refinement: Programming fundamentals, C++, C#, Java, PHP, Web development, Software engineering concepts, Git/GitHub workflow, Building practical applications, Project documentation, and writing clean, maintainable code.

5. DEVELOPER MINDSET SECTION:
   - Present a clear layout message articulating your developmental values: Software development is a continuous process of learning, building, making mistakes, improving, trying again, and growing. Keep it concise, organic, and realistic.

6. CONTACT LINKS FOOTER:
   - Include a clickable email button configured with: mailto:alasastrixie6@gmail.com
   - Include an external resource link out to your project repository: https://github.com

Ensure the layout features clean semantic elements, complete flexbox/grid containers, and standard component sizing. Output ONLY raw HTML syntax text. Do not wrap the response code inside markdown ```html blocks.
"""

try:
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=[{"role": "user", "content": detailed_prompt}]
    )
    clean_html = response.replace("```html", "").replace("```", "").strip()
    with open("index.html", "w") as f:
        f.write(clean_html)
    print("\n[SUCCESS] Your custom portfolio code has been generated!")
except Exception as e:
    print("\n[ERROR] Process halted:", e)
