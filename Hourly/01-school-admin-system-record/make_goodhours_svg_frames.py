from pathlib import Path
import base64

root = Path(__file__).resolve().parent
img_b64 = base64.b64encode((root / 'homepage.png').read_bytes()).decode('ascii')
img_uri = f'data:image/png;base64,{img_b64}'


def save(name: str, content: str) -> None:
    (root / name).write_text(content, encoding='utf-8')

frame1 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="20" stdDeviation="24" flood-color="#0F172A" flood-opacity="0.15"/>
    </filter>
  </defs>
  <rect width="1080" height="1920" fill="url(#g)"/>
  <rect x="0" y="0" width="1080" height="12" fill="#1D4ED8" fill-opacity="0.35"/>
  <rect x="0" y="1910" width="1080" height="10" fill="#D4AF37" fill-opacity="0.55"/>
  <text x="72" y="92" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#1D4ED8">SCHOOL ADMINISTRATOR WORKFLOW</text>
  <text x="72" y="190" font-family="Georgia, Times New Roman, serif" font-size="52" font-weight="700" fill="#0F172A">The trusted system of record</text>
  <text x="72" y="262" font-family="Georgia, Times New Roman, serif" font-size="52" font-weight="700" fill="#0F172A">for student volunteer hours</text>
  <text x="72" y="380" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#334155">Formal tracking for schools that need verified records,</text>
  <text x="72" y="420" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#334155">clear oversight, and clean reporting.</text>
  <text x="92" y="585" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#1E3A8A">• Track service with clarity</text>
  <text x="92" y="625" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#1E3A8A">• Verify records with confidence</text>
  <text x="92" y="665" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#1E3A8A">• Report without spreadsheet chaos</text>
  <rect x="72" y="795" rx="10" ry="10" width="290" height="68" fill="#1D4ED8"/>
  <text x="101" y="838" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Register your school</text>
  <text x="72" y="900" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#64748B">Invitation-only access. Free for schools to start.</text>
  <rect x="620" y="180" width="400" height="900" rx="20" ry="20" fill="#FFFFFF" filter="url(#shadow)"/>
  <image href="{img_uri}" x="640" y="200" width="360" height="860" preserveAspectRatio="xMidYMin slice"/>
</svg>'''

frame2 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F6F9FF"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="20" stdDeviation="24" flood-color="#0F172A" flood-opacity="0.12"/>
    </filter>
  </defs>
  <rect width="1080" height="1920" fill="url(#g)"/>
  <rect x="0" y="0" width="1080" height="10" fill="#1D4ED8" fill-opacity="0.24"/>
  <rect x="0" y="1910" width="1080" height="10" fill="#D4AF37" fill-opacity="0.45"/>
  <text x="72" y="90" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#1D4ED8">GOODHOURS</text>
  <text x="72" y="188" font-family="Georgia, Times New Roman, serif" font-size="58" font-weight="700" fill="#0F172A">One dashboard. One trusted record.</text>
  <text x="72" y="255" font-family="Georgia, Times New Roman, serif" font-size="58" font-weight="700" fill="#0F172A">One formal process.</text>
  <text x="72" y="380" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#334155">GoodHours keeps student hours, approvals, and reporting</text>
  <text x="72" y="418" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#334155">in one school-controlled workflow.</text>

  <rect x="72" y="560" width="220" height="130" rx="14" ry="14" fill="#FFFFFF" filter="url(#shadow)"/>
  <rect x="312" y="560" width="220" height="130" rx="14" ry="14" fill="#FFFFFF" filter="url(#shadow)"/>
  <rect x="72" y="720" width="220" height="130" rx="14" ry="14" fill="#FFFFFF" filter="url(#shadow)"/>
  <text x="92" y="604" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#0F172A">Tracking</text>
  <text x="92" y="638" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#0F172A">Centralized</text>
  <text x="332" y="604" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#0F172A">Verification</text>
  <text x="332" y="638" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#0F172A">Documented</text>
  <text x="92" y="764" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#0F172A">Reporting</text>
  <text x="92" y="798" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#0F172A">Exportable</text>
  <text x="72" y="930" font-family="Arial, Helvetica, sans-serif" font-size="20" fill="#475569">School-controlled records. Clear audit trail. Exportable reporting.</text>

  <rect x="610" y="170" width="398" height="980" rx="20" ry="20" fill="#FFFFFF" filter="url(#shadow)"/>
  <image href="{img_uri}" x="630" y="190" width="358" height="940" preserveAspectRatio="xMidYMin slice"/>
</svg>'''

frame3 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1D4ED8"/>
      <stop offset="100%" stop-color="#163FA3"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="20" stdDeviation="24" flood-color="#001A4D" flood-opacity="0.25"/>
    </filter>
  </defs>
  <rect width="1080" height="1920" fill="url(#g)"/>
  <rect x="0" y="0" width="1080" height="300" fill="#0B2F7D" fill-opacity="0.32"/>
  <rect x="0" y="1620" width="1080" height="300" fill="#D4AF37" fill-opacity="0.18"/>
  <text x="72" y="220" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#FCD34D">FORMAL SCHOOL WORKFLOWS</text>
  <text x="72" y="300" font-family="Georgia, Times New Roman, serif" font-size="58" font-weight="700" fill="#FFFFFF">Bring every hour into one</text>
  <text x="72" y="372" font-family="Georgia, Times New Roman, serif" font-size="58" font-weight="700" fill="#FFFFFF">compliant system.</text>
  <text x="72" y="610" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#E0E7FF">GoodHours is built for school administrators who need a calm,</text>
  <text x="72" y="648" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#E0E7FF">credible way to manage volunteer hours.</text>
  <rect x="72" y="768" width="348" height="72" rx="10" ry="10" fill="#FCD34D" filter="url(#shadow)"/>
  <text x="101" y="814" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#0F172A">Register your school today</text>
  <text x="72" y="1680" font-family="Arial, Helvetica, sans-serif" font-size="19" fill="#DBEAFE">White. Blue. Gold. Clear enough for staff, students, and families.</text>
  <rect x="708" y="260" width="300" height="610" rx="20" ry="20" fill="#FFFFFF" filter="url(#shadow)"/>
  <image href="{img_uri}" x="728" y="280" width="260" height="570" preserveAspectRatio="xMidYMin slice"/>
</svg>'''

save('frame1.svg', frame1)
save('frame2.svg', frame2)
save('frame3.svg', frame3)
print('wrote svg frames')
