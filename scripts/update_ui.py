import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_landing():
    path = os.path.join(BASE_DIR, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update buttons
    if 'Trainer Dashboard' not in content:
        content = content.replace(
            '<a href="deck/index.html?trainer=true" class="card" onclick="alert(\'Trainer mode is active. You can also toggle this anytime in the deck using Shift+T.\');">',
            '<a href="trainer/index.html" class="card">'
        )
        content = content.replace(
            '<p>Launch deck with facilitator notes enabled</p>',
            '<p>Open trainer dashboard and fact checker</p>'
        )
        
        # Add data lab button
        data_lab = """
            <a href="charts/index.html" class="card" target="_blank">
                <h3>DATA LAB</h3>
                <p>View OPL synthetic training data charts</p>
            </a>
        """
        content = content.replace('</div>\n\n        <footer>', data_lab + '\n        </div>\n\n        <footer>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def update_deck():
    path = os.path.join(BASE_DIR, 'deck', 'index.html')
    # Let's write a completely structured presentation that meets all OPL requirements
    
    deck_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OPL Innovate | Microsoft Copilot Training</title>
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
    
    <div id="presentation-container">
        
        <!-- OPEN -->
        <section class="slide active" id="slide-1" data-module="Open">
            <div class="center-all" style="height: 100%;">
                <span class="eyebrow">OPL INNOVATE × Be10x</span>
                <h1>MICROSOFT COPILOT</h1>
                <h2>DAY 2: FROM DATA TO DECISION</h2>
                <div style="margin-top: 4rem;">
                    <p>3 Hours. 5 Core Apps. 3 OPL Data Labs. 4 Case Studies.</p>
                </div>
            </div>
            <div class="slide-footer"><span>Press Space to begin | Shift+T for Trainer Mode</span></div>
        </section>

        <!-- Context -->
        <section class="slide" id="slide-2" data-module="OPL Context" data-trainer-say="Start by rooting this in OPL's actual business.">
            <div class="center-all flex-col" style="height: 100%;">
                <span class="eyebrow">The Business Context</span>
                <h2>OPL is a digital lending infrastructure company.</h2>
                <div class="grid-3" style="margin-top: 2rem;">
                    <div class="card">
                        <h3>235+</h3>
                        <p>Partner Banks</p>
                    </div>
                    <div class="card">
                        <h3>₹6L Cr+</h3>
                        <p>Sanctioned</p>
                    </div>
                    <div class="card">
                        <h3>30L+</h3>
                        <p>MSMEs Onboarded</p>
                    </div>
                </div>
                <div class="source-badge public" style="margin-top:2rem;">[PUBLIC OPL DATA]</div>
            </div>
        </section>
        
        <section class="slide" id="slide-3" data-module="OPL Case" data-trainer-time="5 min">
            <div class="flex-col" style="height: 100%; justify-content: center;">
                <span class="eyebrow">Opening Case</span>
                <h1>The Weekly Operations Review</h1>
                <p>An OPL product team is preparing a weekly review using:</p>
                <ul style="font-size:2rem; line-height:1.8; color:var(--text-secondary); margin-left:2rem;">
                    <li>Excel portfolio metrics</li>
                    <li>Teams meeting notes</li>
                    <li>OAM API report</li>
                </ul>
                <h2 style="margin-top: 2rem; color:var(--warning);">How long would this take manually?</h2>
                <p class="copilot-text" style="font-size:2.5rem; font-weight:bold; margin-top:1rem;">One Business Question. Multiple Copilot Touchpoints.</p>
            </div>
        </section>

        <!-- Prompt Framework -->
        <section class="slide" id="slide-4" data-module="Meet Copilot">
            <div class="flex-col" style="height: 100%; justify-content: center;">
                <span class="eyebrow">OPL Prompt Framework</span>
                <h1>TASK + CONTEXT + SOURCE + CONSTRAINT + OUTPUT + CHECK</h1>
                <div class="grid-2" style="margin-top: 2rem;">
                    <div class="prompt-box bad">"Analyze this loan data."</div>
                    <div class="prompt-box">"You are a lending operations analyst. Using ONLY the attached synthetic MSME portfolio data, identify portfolio growth and high-risk segments. Flag anything requiring human verification."</div>
                </div>
            </div>
        </section>

        <!-- Data Rules -->
        <section class="slide" id="slide-5" data-module="Data Policy" data-trainer-rescue="Emphasize that we do not put real customer data into public AI!">
            <div class="center-all flex-col" style="height: 100%;">
                <h1 style="color: var(--danger);">DATA POLICY</h1>
                <div class="grid-3" style="text-align: left; margin-top:2rem;">
                    <div class="card" style="border-top: 5px solid #10b981;">
                        <h3>PUBLIC FACT</h3>
                        <p>OPL website metrics, brochures.</p>
                    </div>
                    <div class="card" style="border-top: 5px solid var(--warning);">
                        <h3>SYNTHETIC DATA</h3>
                        <p>AI-generated training datasets mimicking OPL workflows.</p>
                    </div>
                    <div class="card" style="border-top: 5px solid var(--danger);">
                        <h3>CONFIDENTIAL DATA</h3>
                        <p>Real internal data. <strong>Do not fabricate this.</strong></p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Apps -->
        <section class="slide" id="slide-6" data-module="Excel">
            <div class="flex-col" style="height: 100%; justify-content: center;">
                <div class="app-header">
                    <div class="app-icon excel">X</div>
                    <h2>Data Lab: MSME Portfolio Intelligence</h2>
                </div>
                <div class="grid-2">
                    <div>
                        <h3>Case Study 1</h3>
                        <p>Open <code>OPL_MSME_CREDIT_PORTFOLIO_TRAINING.csv</code></p>
                        <p><strong>Question:</strong> Where is portfolio risk increasing?</p>
                        <div class="prompt-box" style="margin-top:1rem; font-size:1.5rem;">"Which sector has the highest risk concentration? Provide evidence."</div>
                    </div>
                    <div class="card">
                        <div class="source-badge synthetic">[SYNTHETIC OPL-ALIGNED DATA]</div>
                        <h3 style="margin-top:1rem;">Expected Insights:</h3>
                        <ul style="font-size:1.5rem; color:var(--text-secondary);">
                            <li>High DPD in Retail sector (East region).</li>
                            <li>Average processing TAT outliers.</li>
                            <li>Correlation between cash flow and approval.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="slide" id="slide-7" data-module="Excel">
            <div class="flex-col" style="height: 100%; justify-content: center;">
                <div class="app-header">
                    <div class="app-icon excel">X</div>
                    <h2>Data Lab: Bank Statement Analyzer (BSA)</h2>
                </div>
                <div class="grid-2">
                    <div>
                        <h3>Case Study 2</h3>
                        <p>Open <code>OPL_BANK_STATEMENT_ANALYZER_TRAINING.csv</code></p>
                        <div class="prompt-box" style="margin-top:1rem; font-size:1.5rem;">"Identify transactions flagged as Anomalies. What category are they usually in?"</div>
                    </div>
                    <div class="card">
                        <div class="source-badge synthetic">[SYNTHETIC OPL-ALIGNED DATA]</div>
                        <h3 style="margin-top:1rem;">Verify the output:</h3>
                        <p>Don't let Copilot simply describe the chart. Ask it what evidence supports the conclusion.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="slide" id="slide-8" data-module="Word">
            <div class="flex-col" style="height: 100%; justify-content: center;">
                <div class="app-header">
                    <div class="app-icon word">W</div>
                    <h2>Word: Business Briefs</h2>
                </div>
                <div class="grid-2">
                    <div>
                        <p>Transform raw insights into a structured OPL MSME Portfolio Review document.</p>
                        <div class="prompt-box" style="margin-top:2rem;">"Rewrite this analysis into an executive brief. Sections: Executive Summary, Risk Signals, Next Steps."</div>
                    </div>
                    <div class="card" style="background: rgba(0,0,0,0.2);">
                        <div class="source-badge synthetic">[ILLUSTRATIVE CASE STUDY]</div>
                        <h3 style="margin-top:1rem;">Copilot Output</h3>
                        <p style="font-size:1.2rem; color:#aaa;">(Draft generated successfully based on provided data constraints)</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="slide" id="slide-9" data-module="PowerPoint">
            <div class="flex-col" style="height: 100%; justify-content: center;">
                <div class="app-header">
                    <div class="app-icon powerpoint">P</div>
                    <h2>PowerPoint: OAM+ Architecture Deck</h2>
                </div>
                <div class="grid-2">
                    <div>
                        <p>Using <code>OPL_OAM_Architecture_Brief.docx</code> to generate slides.</p>
                        <div class="prompt-box" style="margin-top:2rem;">"Create a presentation from [file]. Provide speaker notes for each slide."</div>
                    </div>
                    <div class="card" style="display:flex; justify-content:center; align-items:center;">
                        <h2>✨ Deck Generated</h2>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="slide" id="slide-10" data-module="Cross-App">
            <div class="center-all flex-col" style="height: 100%;">
                <span class="eyebrow">The Cross-App Workflow</span>
                <h1>EXECUTIVE DECISION PACK</h1>
                <div style="display: flex; gap: 1rem; align-items: center; justify-content: center; margin-top: 2rem;">
                    <div class="app-icon teams">T</div> <span style="font-size: 2rem;">→</span>
                    <div class="app-icon excel">X</div> <span style="font-size: 2rem;">→</span>
                    <div class="app-icon word">W</div> <span style="font-size: 2rem;">→</span>
                    <div class="app-icon powerpoint">P</div> <span style="font-size: 2rem;">→</span>
                    <div class="app-icon outlook">O</div>
                </div>
                <p style="margin-top: 3rem;">Meeting → Analysis → Brief → Deck → Stakeholder Email</p>
            </div>
        </section>
        
        <section class="slide" id="slide-11" data-module="Human-in-Loop">
            <div class="center-all flex-col" style="height: 100%;">
                <span class="eyebrow">Human In The Loop</span>
                <div class="grid-4" style="display:flex; gap:2rem;">
                    <div class="card" style="text-align:center;"><h3>GENERATE</h3></div>
                    <div class="card" style="text-align:center;"><h3>REVIEW</h3></div>
                    <div class="card" style="text-align:center; border-color:var(--warning);"><h3>VERIFY</h3></div>
                    <div class="card" style="text-align:center; border-color:var(--success);"><h3>DECIDE</h3></div>
                </div>
                <h2 style="margin-top:4rem;">Copilot does the first pass.<br>YOU own the decision.</h2>
            </div>
        </section>

        <!-- UI Overlays -->
        <div id="ui-layer">
            <div style="display: flex; align-items: center;">
                <a href="../index.html" class="ui-btn" style="text-decoration: none; margin-right: 10px;">🏠</a>
                <button class="ui-btn" id="btn-prev">← Previous</button>
            </div>
            
            <div id="timer-container" style="display:none; background:rgba(0,0,0,0.8); padding:10px; border-radius:8px; border:1px solid #333;">
                <button onclick="alert('Timer started: 3 min')">3m</button>
                <button onclick="alert('Timer started: 5 min')">5m</button>
                <button onclick="alert('Timer started: 10 min')">10m</button>
            </div>
            
            <div>
                <button class="ui-btn" onclick="document.getElementById('timer-container').style.display='flex';" style="margin-right: 10px;">⏱</button>
                <button class="ui-btn" onclick="alert('Source: Official OPL Website / Synthetic Data')" style="margin-right: 10px; border-color: var(--warning);">📖 Source</button>
                <button class="ui-btn" id="btn-next">Next →</button>
            </div>
        </div>

        <!-- Trainer Dashboard Overlay -->
        <div id="trainer-overlay">
            <div class="trainer-header">
                <h4>Trainer Mode Active</h4>
            </div>
            <div class="trainer-section">
                <h5>Say</h5><p id="trainer-say">Welcome to Day 2.</p>
                <h5 style="margin-top:10px;">Watch Out</h5><p id="trainer-rescue" style="color:var(--warning);">Ensure they open the correct datasets.</p>
            </div>
        </div>
    </div>

    <script src="js/main.js"></script>
    <script src="js/trainer.js"></script>
</body>
</html>
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(deck_html)


def update_css():
    path = os.path.join(BASE_DIR, 'deck', 'css', 'main.css')
    with open(path, 'a', encoding='utf-8') as f:
        f.write("""
/* OPL Specific Styles appended */
.source-badge {
    padding: 8px 16px;
    border-radius: 4px;
    font-size: 1.2rem;
    font-weight: bold;
    display: inline-block;
}
.source-badge.public { background: #10b981; color: #fff; }
.source-badge.synthetic { background: #F29F05; color: #0B1D3A; }
.source-badge.illustrative { background: #0078d4; color: #fff; }
""")

if __name__ == '__main__':
    update_landing()
    update_deck()
    update_css()
    print("UI update complete.")
