
import g4f

print("Connecting to AI... Generating Trixie's Multi-Image Portfolio...")

detailed_prompt = """
Write a single-file, highly polished, fully responsive modern developer portfolio website using valid HTML5 and Tailwind CSS via its CDN link.

Apply these explicit visual layout configurations:
- Visual Theme: Professional coding aesthetic with a gorgeous GRADIENT pastel blue background layout theme. 
- Styling Traits: Clean professional typography, balanced layout spacing, strategic tech-focused icon badges, subtle hover micro-interactions, no massive walls of text.

Incorporate this exact structural content:
1. HERO INTRO SECTION:
   - Primary Display Name: Trixie B. Alas-as
   - Headline Title: Fresh BSIT Graduate • Aspiring Software Engineer   - Text Introduction: "Hi, I'm Trixie Alas-as, a second-year BSIT (Bachelor of Science in Information Technology) student. As I continue my college journey, I want to improve my knowledge and become more confident in using technology. I'm interested in learning different skills, especially through activities, projects, and hands-on experiences in school. I know that I still have a lot to learn, so I'm willing to listen to advice, learn from my mistakes, and keep improving. I'm looking forward to gaining more experience and developing the skills I need for my future career in Information Technology."

2. CORE TECH STACK SECTION:
   - Header Section Title: "Technologies I have worked with"
   - Languages: C++, Java, PHP, HTML, CSS (Beginner / Entry-Level skills).
   - Tools & Environment: VS Code, Git, GitHub, Canva, Microsoft Office.

3. FEATURED WORK & PROJECTS GRID (Display ALL 3 images per project!):
   - Include 3 distinct interactive layout cards linking to your local folders. Inside each card, right above the description text, include a grid of ALL 3 images belonging to that project using Tailwind CSS styling (`grid grid-cols-3 gap-1 rounded-t-xl overflow-hidden`).
   
     * Card 1: AFTER_EXAM
       Show these 3 images side-by-side inside this card's top header:
       1. ./AFTER_EXAM/IMG_20260927_214305.jpg
       2. ./AFTER_EXAM/received_1107371708923598.jpeg
       3. ./AFTER_EXAM/received_1490559959516250.jpeg
       Description text: "A collection of core programming logic, algorithms, and application builds created immediately following key academic examinations to test comprehensive module understanding."
       Link destination button: ./AFTER_EXAM/index.html
       
     * Card 2: NSTP
       Show these 3 images side-by-side inside this card's top header:
       1. ./NSTP/received_826579790059784.jpeg
       2. ./NSTP/received_919240214481492.jpeg
       3. ./NSTP/received_931365109664706.jpeg
       Description text: "Digital documentation, community project layouts, and civic action reports compiled in fulfillment of the National Service Training Program requirements."
       Link destination button: ./NSTP/index.html
       
     * Card 3: VLOG
       Show these 3 images side-by-side inside this card's top header:
       1. ./VLOG/received_1651188139653877.jpeg
       2. ./VLOG/received_912928448027213.jpeg
       3. ./VLOG/received_964291302601711.jpeg
       Description text: "A dynamic video presentation and media project mapping out practical technology concepts, tutorial walk-throughs, and academic college life experiences."
       Link destination button: ./VLOG/index.html

   - Include a primary anchor badge button linking directly to your main repository deployment: https://github.io

4. CURRENTLY LEARNING SECTION:
   - Display a list focusing on continuous skill refinement: Programming fundamentals, C++, C#, Java, PHP, Web development, Software engineering concepts, Git/GitHub workflow, Building practical applications, Project documentation, and writing clean, maintainable code.

5. DEVELOPER MINDSET SECTION:
   - Present a clear layout message articulating your developmental values.

6. CONTACT LINKS FOOTER:
   - Include a clickable email button configured with: mailto:alasastrixie6@gmail.com
   - Include an external resource link out to your project repository: https://github.com

Ensure the layout features clean semantic elements, complete flexbox/grid containers, and standard image scaling. Output ONLY raw HTML syntax text. Do not wrap the response code inside markdown ```html blocks.
"""

try:
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=[{"role": "user", "content": detailed_prompt}]
    )
    clean_html = response.replace("```html", "").replace("```", "").strip()
    with open("index.html", "w") as f:
        f.write(clean_html)
    print("\n[SUCCESS] Website code updated! All 9 project images are now added to the grid!")
except Exception as e:
    print("\n[ERROR] Process halted:", e)









