import csv, json, hashlib, xml.etree.ElementTree as ET
from pathlib import Path
root=Path(__file__).resolve().parents[1]
import argparse
parser=argparse.ArgumentParser(description='Verify curated component candidates against an independently downloaded Arcticons appfilter.')
parser.add_argument('reference', type=Path)
reference=parser.parse_args().reference
# Requested order in the approved 8 x 5 reference sheet; the two omitted apps keep their source-cell positions.
rows=[
('phone','Téléphone',0,'com.samsung.android.dialer',['com.samsung.android.dialer.DialtactsActivity']),
('messages','Messages',1,'com.samsung.android.messaging',['com.android.mms.ui.ConversationComposer','com.samsung.android.messaging.ui.ConversationListActivity','com.samsung.android.messaging.ui.ConversationList']),
('contacts','Contacts',2,'com.samsung.android.contacts',['com.android.contacts.activities.PeopleActivity','com.samsung.android.contacts.contactslist.PeopleActivity']),
('calendar','Calendrier',3,'com.samsung.android.calendar',['com.android.calendar.AllInOneActivity','com.samsung.android.app.calendar.activity.MainActivity']),
('camera','Appareil photo',4,'com.sec.android.app.camera',['com.sec.android.app.camera.Camera']),
('gallery','Galerie',5,'com.sec.android.gallery3d',['com.sec.android.gallery3d.app.GalleryOpaqueActivity','com.samsung.android.gallery.app.activity.GalleryActivity']),
('files','Mes fichiers',6,'com.sec.android.app.myfiles',['com.sec.android.app.myfiles.external.ui.MainActivity','com.sec.android.app.myfiles.external.ui.LaunchActivity','com.sec.android.app.myfiles.common.MainActivity']),
('settings','Paramètres',7,'com.android.settings',['com.android.settings.Settings']),
('chrome','Chrome',8,'com.android.chrome',['com.google.android.apps.chrome.Main','com.android.chrome.Main']),
('google','Google',9,'com.google.android.googlequicksearchbox',['com.google.android.googlequicksearchbox.SearchActivity','com.google.android.googlequicksearchbox.GoogleSearch']),
('play_store','Play Store',10,'com.android.vending',['com.android.vending.AssetBrowserActivity','com.google.android.finsky.activities.PlayLauncherActivity']),
('youtube','YouTube',11,'com.google.android.youtube',['com.google.android.youtube.app.honeycomb.Shell$HomeActivity','com.google.android.youtube.app.honeycomb.Shell']),
('spotify','Spotify',12,'com.spotify.music',['com.spotify.music.MainActivity','com.spotify.music.main.MainScreenActivity']),
('tiktok','TikTok',13,'com.zhiliaoapp.musically',['com.zhiliaoapp.musically.MainActivity','com.ss.android.ugc.aweme.splash.SplashActivity','com.ss.android.ugc.trill.splash.I18nSplashActivity','com.zhiliaoapp.musically.activity.SplashActivity']),
('chatgpt','ChatGPT',14,'com.openai.chatgpt',['com.openai.chatgpt.MainActivity']),
('gemini','Gemini',15,'com.google.android.apps.bard',['com.google.android.apps.bard.shellapp.BardEntryPointActivity']),
('outlook','Outlook',16,'com.microsoft.office.outlook',['com.microsoft.office.outlook.MainActivity','com.microsoft.office.outlook.ui.miit.MiitLauncherActivity']),
('gmail','Gmail',17,'com.google.android.gm',['com.google.android.gm.ConversationListActivityGmail']),
('drive','Drive',18,'com.google.android.apps.docs',['com.google.android.apps.docs.app.NewMainProxyActivity','com.google.android.apps.docs.app.HomeScreenActivity','com.google.android.apps.docs.app.MainProxyActivity']),
('photos','Photos',19,'com.google.android.apps.photos',['com.google.android.apps.photos.home.HomeActivity']),
('maps','Maps',20,'com.google.android.apps.maps',['com.google.android.maps.MapsActivity']),
('google_tv','Google TV',21,'com.google.android.videos',['com.google.android.videos.activity.HomeActivity','com.google.android.videos.activity.LauncherActivity','com.google.android.youtube.videos.EntryPoint']),
('shazam','Shazam',22,'com.shazam.android',['com.shazam.android.activities.SplashActivity','com.shazam.android.activities.MainActivity']),
('youtube_music','YouTube Music',23,'com.google.android.apps.youtube.music',['com.google.android.apps.youtube.music.activities.MusicActivity']),
('samsung_notes','Samsung Notes',24,'com.samsung.android.app.notes',['com.samsung.android.app.notes.memolist.MemoListActivity']),
('clock','Horloge',25,'com.sec.android.app.clockpackage',['com.sec.android.app.clockpackage.ClockPackage','com.sec.android.app.clockpackage.common.activity.ClockPackage']),
('calculator','Calculatrice',26,'com.sec.android.app.popupcalculator',['com.sec.android.app.popupcalculator.Calculator']),
('bixby','Bixby',27,'com.samsung.android.bixby.agent',['com.samsung.android.bixby.assistanthome.AssistantHomeLauncherActivity','com.samsung.android.bixby.assistanthome.AssistantHomeMainActivity']),
('samsung_health','Samsung Health',28,'com.sec.android.app.shealth',['com.samsung.android.app.shealth.home.HomeMainActivity','com.samsung.android.app.shealth.home.HomeDashboardActivity']),
('galaxy_store','Galaxy Store',29,'com.sec.android.app.samsungapps',['com.sec.android.app.samsungapps.SamsungAppsMainActivity','com.sec.android.app.samsungapps.Main','com.sec.android.app.samsungapps.SKSamsungMainActivity']),
('good_lock','Good Lock',30,'com.samsung.android.goodlock',['com.samsung.android.goodlock.MainActivity','com.samsung.android.goodlock.presentation.view.LaunchActivity','com.samsung.android.goodlock.presentation.view.PluginListActivity']),
('samsung_members','Samsung Members',31,'com.samsung.android.voc',['com.samsung.android.voc.app.LauncherActivity','com.samsung.android.voc.MainActivity','com.samsung.android.voc.LauncherActivity']),
('meet','Meet',32,'com.google.android.apps.tachyon',['com.google.android.apps.tachyon.MainActivitySecondLauncher','com.google.android.apps.tachyon.MainActivity']),
('vlc','VLC',34,'org.videolan.vlc',['org.videolan.vlc.StartActivity','org.videolan.vlc.gui.MainActivity']),
('linkedin','LinkedIn',35,'com.linkedin.android',['com.linkedin.android.authenticator.LaunchActivity','com.linkedin.android.authenticator.LaunchActivityDefault','com.linkedin.android.MainActivity']),
('alexa','Amazon Alexa',36,'com.amazon.dee.app',['com.amazon.dee.app.Launcher','com.amazon.dee.webapp.activity.AlexaWebAppActivity']),
('leboncoin','leboncoin',38,'fr.leboncoin',['fr.leboncoin.feature.splashscreen.ui.activities.SplashScreenActivity','fr.leboncoin.ui.activities.SplashScreenActivity','fr.leboncoin.splashscreen.ui.activities.SplashScreenActivity','fr.leboncoin.features.splashscreen.ui.activities.SplashScreenActivity']),
('icon_pack_studio','Icon Pack Studio',39,'ginlemon.iconpackstudio',['ginlemon.iconpackstudio.editor.homeActivity.HomeActivity'])]
# Normalize short Android class names before comparing to the independent source.
known=set()
for it in ET.parse(reference).getroot().findall('item'):
 c=it.get('component','')[14:-1]
 if '/' not in c: continue
 p,a=c.split('/',1)
 known.add((p,p+a if a.startswith('.') else a))
items=[]; maps=[]
for key,label,cell,pkg,activities in rows:
 items.append(dict(key=key,label=label,source_cell=cell,asset='helix_'+key,package=pkg))
 for activity in activities:
  assert (pkg,activity) in known,(pkg,activity)
  maps.append([key,label,pkg,activity,'helix_'+key])
(root/'catalog.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (root/'app-map.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.writer(f);w.writerow(['helix_key','label','package_name','component','asset']);w.writerows(maps)
(root/'mapping-evidence.json').write_text(json.dumps(dict(source='https://github.com/Arcticons-Team/Arcticons/blob/main/app/src/main/res/xml/appfilter.xml',retrieved='2026-09-25',source_sha256=hashlib.sha256(reference.read_bytes()).hexdigest(),status='Corroborated by public icon-pack source; physical S24 launch components not yet tested',mappings=[dict(package_name=m[2],component=m[3],asset=m[4]) for m in maps],excluded_unverified=[dict(package_name='com.samsung.android.messaging',component='com.samsung.android.messaging.ui.view.main.WithActivity',reason='Initial pilot candidate not corroborated; confirm on S24 before restoring')]),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(items),'icons;',len(maps),'corroborated mappings')
