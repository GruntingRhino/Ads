from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
screenshot = root / 'homepage.png'

font_serif = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
font_sans = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font_sans_bold = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

texts = {
    'frame1_headline.txt': 'The trusted system of record\nfor student volunteer hours',
    'frame1_sub.txt': 'Formal tracking for schools that need verified records,\nclear oversight, and clean reporting.',
    'frame1_bullets.txt': '• Track service with clarity\n• Verify records with confidence\n• Report without spreadsheet chaos',
    'frame1_cta.txt': 'Register your school',
    'frame1_tag.txt': 'School administrator workflow',
    'frame2_headline.txt': 'One dashboard. One trusted record.\nOne formal process.',
    'frame2_sub.txt': 'GoodHours keeps student hours, approvals, and reporting in one school-controlled workflow.',
    'frame2_left_a.txt': 'Tracking\nCentralized',
    'frame2_left_b.txt': 'Verification\nDocumented',
    'frame2_left_c.txt': 'Reporting\nExportable',
    'frame2_note.txt': 'School-controlled records. Clear audit trail. Exportable reporting.',
    'frame3_tag.txt': 'Designed for formal school workflows',
    'frame3_headline.txt': 'Bring every hour into one\ncompliant system.',
    'frame3_sub.txt': 'GoodHours is built for school administrators who need a calm, credible way to manage volunteer hours.',
    'frame3_cta.txt': 'Register your school today',
    'frame3_note.txt': 'White. Blue. Gold. Clear enough for staff, students, and families.',
}
for name, content in texts.items():
    (root / name).write_text(content + '\n')


def run(cmd):
    subprocess.run(cmd, check=True)

# Frame 1
run([
    'ffmpeg', '-y',
    '-f', 'lavfi', '-i', 'color=c=white:s=1080x1920',
    '-i', str(screenshot),
    '-filter_complex',
    (
        f"[0:v]drawbox=x=0:y=0:w=1080:h=1920:color=F8FAFC@1:t=fill,"
        f"drawbox=x=0:y=0:w=1080:h=12:color=1D4ED8@0.35:t=fill,"
        f"drawbox=x=0:y=1910:w=1080:h=12:color=D4AF37@0.5:t=fill[bg];"
        f"[1:v]crop=788:1200:0:0,scale=390:-1[shot];"
        f"[bg]drawbox=x=72:y=180:w=430:h=900:color=white@1:t=fill,"
        f"drawbox=x=72:y=180:w=430:h=900:color=E2E8F0@1:t=2[card];"
        f"[card][shot]overlay=92:210[tmp1];"
        f"[tmp1]drawtext=fontfile={font_sans_bold}:textfile={root/'frame1_tag.txt'}:fontsize=24:fontcolor=1D4ED8:x=72:y=78,"
        f"drawtext=fontfile={font_serif}:textfile={root/'frame1_headline.txt'}:fontsize=64:line_spacing=12:fontcolor=0F172A:x=72:y=150,"
        f"drawtext=fontfile={font_sans}:textfile={root/'frame1_sub.txt'}:fontsize=25:line_spacing=8:fontcolor=334155:x=72:y=485,"
        f"drawtext=fontfile={font_sans_bold}:textfile={root/'frame1_bullets.txt'}:fontsize=22:line_spacing=16:fontcolor=1E3A8A:x=72:y=610,"
        f"drawbox=x=72:y=805:w=270:h=68:color=1D4ED8@1:t=fill,"
        f"drawtext=fontfile={font_sans_bold}:textfile={root/'frame1_cta.txt'}:fontsize=24:fontcolor=FFFFFF:x=103:y=824,"
        f"drawtext=fontfile={font_sans}:text='Invitation-only access. Free for schools to start.':fontsize=18:fontcolor=475569:x=72:y=900"
    ),
    '-frames:v', '1', str(root / 'frame1.png')
])

# Frame 2
run([
    'ffmpeg', '-y',
    '-f', 'lavfi', '-i', 'color=c=F6F9FF:s=1080x1920',
    '-i', str(screenshot),
    '-filter_complex',
    (
        f"[0:v]drawbox=x=0:y=0:w=1080:h=1920:color=F6F9FF@1:t=fill,"
        f"drawbox=x=0:y=0:w=1080:h=10:color=1D4ED8@0.24:t=fill,"
        f"drawbox=x=0:y=1910:w=1080:h=10:color=D4AF37@0.45:t=fill[bg];"
        f"[1:v]crop=788:980:0:360,scale=390:-1[shot];"
        f"[bg]drawbox=x=610:y=170:w=398:h=980:color=white@1:t=fill,"
        f"drawbox=x=610:y=170:w=398:h=980:color=CBD5E1@1:t=2[card];"
        f"[card][shot]overlay=622:192[tmp1];"
        f"[tmp1]drawtext=fontfile={font_sans_bold}:text='GOODHOURS':fontsize=22:fontcolor=1D4ED8:x=72:y=86,"
        f"drawtext=fontfile={font_serif}:textfile={root/'frame2_headline.txt'}:fontsize=56:line_spacing=12:fontcolor=0F172A:x=72:y=150,"
        f"drawtext=fontfile={font_sans}:textfile={root/'frame2_sub.txt'}:fontsize=24:line_spacing=8:fontcolor=334155:x=72:y=425,"
        f"drawbox=x=72:y=560:w=220:h=130:color=FFFFFF@1:t=fill,drawbox=x=72:y=560:w=220:h=130:color=DBE4F0@1:t=2,"
        f"drawbox=x=312:y=560:w=220:h=130:color=FFFFFF@1:t=fill,drawbox=x=312:y=560:w=220:h=130:color=DBE4F0@1:t=2,"
        f"drawbox=x=72:y=720:w=220:h=130:color=FFFFFF@1:t=fill,drawbox=x=72:y=720:w=220:h=130:color=DBE4F0@1:t=2,"
        f"drawtext=fontfile={font_sans_bold}:textfile={root/'frame2_left_a.txt'}:fontsize=22:line_spacing=4:fontcolor=0F172A:x=92:y=592,"
        f"drawtext=fontfile={font_sans_bold}:textfile={root/'frame2_left_b.txt'}:fontsize=22:line_spacing=4:fontcolor=0F172A:x=332:y=592,"
        f"drawtext=fontfile={font_sans_bold}:textfile={root/'frame2_left_c.txt'}:fontsize=22:line_spacing=4:fontcolor=0F172A:x=92:y=752,"
        f"drawtext=fontfile={font_sans}:textfile={root/'frame2_note.txt'}:fontsize=20:line_spacing=8:fontcolor=475569:x=72:y=900"
    ),
    '-frames:v', '1', str(root / 'frame2.png')
])

# Frame 3
run([
    'ffmpeg', '-y',
    '-f', 'lavfi', '-i', 'color=c=1D4ED8:s=1080x1920',
    '-i', str(screenshot),
    '-filter_complex',
    (
        f"[0:v]drawbox=x=0:y=0:w=1080:h=1920:color=1D4ED8@1:t=fill,"
        f"drawbox=x=0:y=0:w=1080:h=300:color=0B2F7D@0.32:t=fill,"
        f"drawbox=x=0:y=1620:w=1080:h=300:color=D4AF37@0.18:t=fill[bg];"
        f"[1:v]crop=788:720:0:0,scale=300:-1[shot];"
        f"[bg]drawbox=x=708:y=260:w=300:h=610:color=FFFFFF@1:t=fill,"
        f"drawbox=x=708:y=260:w=300:h=610:color=EAB308@0.22:t=2[card];"
        f"[card][shot]overlay=728:280[tmp1];"
        f"[tmp1]drawtext=fontfile={font_sans_bold}:textfile={root/'frame3_tag.txt'}:fontsize=22:fontcolor=FCD34D:x=72:y=220,"
        f"drawtext=fontfile={font_serif}:textfile={root/'frame3_headline.txt'}:fontsize=64:line_spacing=12:fontcolor=FFFFFF:x=72:y=290,"
        f"drawtext=fontfile={font_sans}:textfile={root/'frame3_sub.txt'}:fontsize=24:line_spacing=8:fontcolor=E0E7FF:x=72:y=610,"
        f"drawbox=x=72:y=770:w=330:h=72:color=FCD34D@1:t=fill,"
        f"drawtext=fontfile={font_sans_bold}:textfile={root/'frame3_cta.txt'}:fontsize=24:fontcolor=0F172A:x=101:y=790,"
        f"drawtext=fontfile={font_sans}:textfile={root/'frame3_note.txt'}:fontsize=19:fontcolor=DBEAFE:x=72:y=1680"
    ),
    '-frames:v', '1', str(root / 'frame3.png')
])

# Build per-scene clips and final video.
scenes = [('frame1.png', 8), ('frame2.png', 8), ('frame3.png', 10)]
scene_videos = []
for idx, (img, dur) in enumerate(scenes, start=1):
    out = root / f'scene{idx}.mp4'
    run([
        'ffmpeg', '-y',
        '-loop', '1', '-i', str(root / img),
        '-t', str(dur),
        '-r', '30',
        '-vf', 'scale=1080:1920,format=yuv420p',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        str(out)
    ])
    scene_videos.append(out)

concat_list = root / 'concat.txt'
concat_list.write_text(''.join(f"file '{p.name}'\n" for p in scene_videos))
run([
    'ffmpeg', '-y',
    '-f', 'concat', '-safe', '0', '-i', str(concat_list),
    '-c', 'copy',
    str(root / 'video_silent.mp4')
])
run([
    'ffmpeg', '-y',
    '-i', str(root / 'video_silent.mp4'),
    '-i', str(root / 'voiceover.mp3'),
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-shortest',
    str(root / 'final.mp4')
])

# Derived screenshot for quick review.
run([
    'ffmpeg', '-y',
    '-i', str(root / 'final.mp4'),
    '-ss', '00:00:09',
    '-frames:v', '1',
    str(root / 'screenshot.png')
])

print('done')
