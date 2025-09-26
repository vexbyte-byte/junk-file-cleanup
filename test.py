import os

formatted_text = ""

cache =[
    # Tng
    'my.com.tngdigital.ewallet', 
    'my.com.tngdigital.ewallet.ui.SplashActivity',
    # Canon Print
    'jp.co.canon.bsd.ad.pixmaprint',
    'jp.co.canon.bsd.ad.pixmaprint.EulaActivity',
    # Avast Secure Browser
    'com.avast.android.secure.browser',
    'com.tenta.android.activities.MainActivity',
    # Instagram
    'com.instagram.android',
    'com.instagram.android.activity.MainTabActivity',
    # Chess
    'com.chess',
    'com.chess.splash.SplashActivity',
    # Termux
    'com.termux',
    'com.termux.app.TermuxActivity',
    # Roblox
    'com.roblox.client',
    'com.roblox.client.startup.ActivitySplash',
    # Inshot
    'com.inshot.screenrecorder.activities.SplashBeforeActivity',
    # blackbox
    'com.blackbox.blackboxapp',
    'com.blackbox.blackboxapp.MainActivity',
    # InShot
    'com.camerasideas.instashot',
    'com.camerasideas.instashot.MainActivity',
    # Threads
    'com.instagram.barcelona',
    'com.instagram.barcelona.mainactivity.BarcelonaActivity',
    # Gemini
    'com.google.android.apps.bard',
    'com.google.android.apps.bard.shellapp.BardEntryPointActivity',
    # Speedtest
    'org.zwanoo.android.speedtest',
    'com.ookla.mobile4.screens.main.MainActivity',
    # Brawl Stars
    'com.supercell.brawlstars',
    'com.supercell.brawlstars.GameApp',
    # Photos
    'com.google.android.apps.photos',
    'com.google.android.apps.photos.home.HomeActivity',
    # Drive
    'com.google.android.apps.docs',
    'com.google.android.apps.docs.app.NewMainProxyActivity',
    # Samsung Notes
    'com.samsung.android.app.notes',
    'com.samsung.android.app.notes.memolist.MemoListActivity',
    # Discord
    'com.discord',
    'com.discord.main.MainDefault',
    # Kaspersky
    'com.kms.free',
    'com.kms.free.PermissionsActivityLauncher',
    # Hotlink
    'my.com.maxis.hotlink.production',
    'my.com.maxis.hotlink.RevampMainActivity',
    # Spotify
    'com.spotify.music',
    'com.spotify.music.MainActivity',
    # Malwarebytes
    'org.malwarebytes.antimalware',
    'org.malwarebytes.antimalware.ui.MainActivity',
    # Sticker.ly
    'com.snowcorp.stickerly.android',
    'com.snowcorp.stickerly.android.LauncherEntryActivity',
    # Pydroid 3
    'ru.iiec.pydroid3',
    'ru.iiec.pydroid.MainActivity',
    # Spck Editor
    'io.spck',
    'io.spck.editor.EditorActivity',
    # Telegram
    'org.telegram.messenger.web',
    'org.telegram.messenger.DefaultIcon',
    ]

data = [
    # Ultimate USB
    'com.mixapplications.ultimateusb',
    'com.mixapplications.ultimateusb.MainActivity',
    # XRecorder
    'videoeditor.videorecorder.screenrecorder',
    # Heart Rate - SpO2
    'com.heartbeattracker.pulseoximeter.heartrate',
    'com.heartbeattracker.pulseoximeter.heartrate.ui.activitis.SplashActivity',
    # ZArchiver
    'ru.zdevs.zarchiver',
    'ru.zdevs.zarchiver.ZArchiver'
    # Synthesia
    'com.synthesia.synthesia',
    'com.synthesia.synthesia.SynthesiaActivity',
    # ChatGPT
    'com.openai.chatgpt',
    'com.openai.chatgpt.MainActivity',
    # Calculator
    'com.sec.android.app.popupcalculator',
    'com.sec.android.app.popupcalculator.Calculator',
    # Package Names
    'com.csdroid.pkg',
    'com.csdroid.pkg.MainActivity',
    # Supreme Duelist Stickman
    'com.Neurononfire.SupremeDuelist',
    'com.google.firebase.MessagingUnityPlayerActivity',
    # Droid Tesla
    'org.vlada.droidtesla',
    'org.vlada.droidteslapro.MainActivity',
    # Acode
    'com.foxdebug.acode',
    'com.foxdebug.acode.MainActivity',
    # F-Droid
    'org.fdroid.fdroid',
    'org.fdroid.fdroid.views.main.MainActivity',
    # PROTO
    'com.proto.circuitsimulator',
    'com.proto.circuitsimulator.splash.SplashActivity',
    # Magnetic Field Counter
    'com.keuwl.magneticfieldcounter',
    'com.keuwl.magneticfieldcounter.MainActivity',
    # CircuitSafari
    'com.logipipe.circuitsafari',
    'com.logipipe.circuitsafari.FullscreenActivity',
]

text = """
WhatsApp
com.whatsapp
com.whatsapp.Main

Ampere
com.gombosdev.ampere
com.gombosdev.ampere.MainActivity

AdGuard
com.adguard.android
com.adguard.android.ui.activity.SplashActivity

Cxxdroid

ru.iiec.cxxdroid

ru.iiec.cxxdroid.CxxActivity

Android System SafetyCore
com.google.android.safetycore

null

VirusTotal

org.chromium.webapk.a1d8342e5ce2b8837_v2

org.chromium.webapk.shell_apk.h2o.H2OOpaqueMainActivity

Waze
com.waze
com.waze.FreeMapAppActivity

Avast Mobile Security
com.avast.android.mobilesecurity
com.avast.android.one.base.ui.main.MainActivity

Android System Key Verifier
com.google.android.contactkeys

null

EveryCircuit
com.everycircuit.free
com.everycircuit.HomeLauncher

TikTok
com.ss.android.ugc.trill
com.ss.android.ugc.aweme.splash.SplashActivity

DeepSeek
com.deepseek.chat
com.deepseek.chat.MainActivity

My Files
com.sec.android.app.myfiles
com.sec.android.app.myfiles.external.ui.MainActivity

Storage Manager
com.android.storagemanager

null

Print Spooler
com.android.printspooler

null

SIM toolkit
com.android.stk2

null

Samsung Cloud
com.samsung.android.scloud

null

Ad Privacy
com.google.android.adservices.api

null

SettingsBixby
com.samsung.android.app.settings.bixby

null

Group Sharing
com.samsung.android.mobileservice

null

Samsung Cloud Assistant
com.samsung.android.scpm

null

android.auto_generated_rro_vendor__

android.auto_generated_rro_vendor__

null

PacProcessor
com.android.pacprocessor

null

Safety information
com.samsung.safetyinformation

null

Locale Overlay Manager
com.samsung.android.localeoverlaymanager

null
com.google.android.overlay.modules.captiveportallogin.forframework
com.google.android.overlay.modules.captiveportallogin.forframework

null

CSC
com.samsung.sec.android.application.csc

null

Service mode
com.sec.android.app.servicemodeapp

null

Android Switch
com.google.android.apps.restore

null

Live Wallpaper Picker
com.android.wallpaper.livepicker

null
com.google.android.overlay.modules.permissioncontroller.forframework
com.google.android.overlay.modules.permissioncontroller.forframework

null
com.sec.bcservice
com.sec.bcservice

null

Gestural Navigation Bar
com.android.internal.systemui.navbar.gestural_narrow_back

null

Cell Broadcast Service
com.google.android.cellbroadcastservice

null

One UI Home
com.sec.android.app.launcher

null

Google Partner Setup
com.google.android.partnersetup

null

Phone and Messaging Storage
com.android.providers.telephony

null

Waterfall cutout
com.android.internal.display.cutout.emulation.waterfall

null
com.samsung.android.wifi.resources
com.samsung.android.wifi.resources

null

Google Safety Center Resources
com.google.android.safetycenter.resources

null

EmergencyProvider
com.sec.android.provider.emergencymode

null

Speech Services by Google
com.google.android.tts

null

Smart Switch Agent
com.sec.android.easyMover.Agent

null

SetupWizardLegalProvider
com.sec.android.app.setupwizardlegalprovider

null

Emergency SOS
com.samsung.android.emergency

null
com.android.ondevicepersonalization.services.OnDevicePersonalizationApplication
com.google.android.ondevicepersonalization.services

null

Android Shared Library
com.google.android.ext.shared

null

FactoryAPP
com.val.hardware

null

Enterprise Sim Pin Service
com.sec.enterprise.mdm.services.simpin

null

KeyCustomizationInfoBNR
com.samsung.android.keycustomizationinfobackupservice

null
com.android.cts.ctsshim
com.android.cts.ctsshim

null
com.samsung.android.wifi.softap.resources
com.samsung.android.wifi.softap.resources

null

MTP Host
com.android.mtp

null

System Connectivity Resources
com.google.android.connectivity.resources

null

ClipboardSaveService
com.samsung.clipboardsaveservice

null

AudioMirroring
com.samsung.android.audiomirroring

null

Bookmark Provider
com.android.bookmarkprovider

null

Quick Share
com.samsung.android.app.sharelive

null

Samsung Push Service
com.sec.spp.push

null

SamsungOne
com.monotype.android.font.samsungone

null

RilNotifier
com.sec.app.RilErrorNotifier

null

CarrierDefaultApp
com.android.carrierdefaultapp

null

Support components
com.google.mainline.telemetry

null

Fused Location
com.android.location.fused

null

Gestural Navigation Bar
com.android.internal.systemui.navbar.gestural_extra_wide_back

null
com.android.localtransport
com.android.localtransport

null

Samsung Core Services
com.samsung.android.scs

null

Configuration message
com.wsomacp

null

Gestural Navigation Bar
com.samsung.internal.systemui.navbar.gestural_no_hint

null
com.google.android.overlay.modules.cellbroadcastreceiver
com.google.android.overlay.modules.cellbroadcastreceiver

null

Tasks
com.samsung.android.app.taskedge

null

Companion Device Manager
com.android.companiondevicemanager

null

System UWB Resources
com.android.uwb.resources

null

Wireless emergency alerts
com.google.android.cellbroadcastreceiver

null

Call
com.samsung.android.incallui

null

Tethering
com.google.android.networkstack.tethering

null

Basic Daydreams
com.android.dreams.basic

null

Reminder
com.samsung.android.app.reminder

null
com.google.android.overlay.modules.documentsui
com.google.android.overlay.modules.documentsui

null

Gestural Navigation Bar
com.android.internal.systemui.navbar.gestural_wide_back

null

Software update
com.wssyncmldm

null
com.google.android.overlay.gmsconfig.gsa
com.google.android.overlay.gmsconfig.gsa

null

Calendar
com.samsung.android.calendar
com.samsung.android.app.calendar.activity.MainActivity

Editor Lite
com.samsung.app.newtrim

null

CallBGProvider
com.samsung.android.callbgprovider

null

Photo Editor
com.sec.android.mimage.photoretouching

null

Samsung capture
com.samsung.android.app.smartcapture

null

Shell
com.android.shell

null

User manual
com.sec.android.widgetapp.webmanual

null

DQA
com.samsung.android.dqagent

null

App update
com.samsung.android.app.updatecenter

null

Google Location History
com.google.android.gms.location.history

null

User Dictionary
com.android.providers.userdictionary

null
com.android.wifi.dialog
com.android.wifi.dialog

null

Market Feedback Agent
com.google.android.feedback

null

Settings Suggestions
com.android.settings.intelligence

null

Photos & videos
com.google.android.photopicker

null
com.google.android.federatedcompute
com.google.android.federatedcompute

null

Bluetooth MIDI Service
com.android.bluetoothmidiservice

null
com.android.carrierconfig
com.android.carrierconfig

null

Double cutout
com.android.internal.display.cutout.emulation.double

null

Android System WebView
com.google.android.webview

null

One Handed Mode
com.android.internal.systemui.onehanded.gestural

null

Print Service Recommendation Service
com.google.android.printservice.recommendation

null

Apps
com.samsung.android.app.appsedge

null

Camera
com.sec.android.app.camera
com.sec.android.app.camera.Camera

Quick Share Agent
com.samsung.android.aware.service

null

Application recommendations
com.samsung.android.mapsagent

null

Samsung Keyboard
com.samsung.android.honeyboard

null

Wallpaper and style
com.samsung.android.app.dressroom

null

SimMobilityKit
com.samsung.ims.smk

null

Device care
com.samsung.android.lool

null

Galaxy Themes Service
com.samsung.android.themecenter

null

Contacts Storage
com.samsung.android.providers.contacts

null

ContainerService
com.samsung.android.container

null

External Storage
com.android.externalstorage

null

Video Player
com.samsung.android.video

null
com.sec.epdg
com.sec.epdg

null

EpdgTestApp
com.sec.epdgtestapp

null

Hiya Service
com.hiya.star

null

Device security
com.samsung.android.sm.devicesecurity

null

Quick Share Connectivity
com.samsung.android.mdx.kit

null

NetworkDiagnostic
com.samsung.android.networkdiagnostic

null

Key Chain
com.android.keychain

null
com.google.android.overlay.gmsconfig.geotz
com.google.android.overlay.gmsconfig.geotz

null

Work Setup
com.android.managedprovisioning

null

Perso
com.sec.android.app.personalization

null

IMS Service
com.sec.imsservice

null

SecurityPolicy
com.samsung.aasaservice

null

Find My Mobile
com.samsung.android.fmm

null

People
com.samsung.android.service.peoplestripe

null

Service mode RIL
com.sec.android.RilServiceModeApp

null

RcsSettings
com.samsung.rcs

null

Android System

android

null

Google Play services
com.google.android.gms

null

Software update
com.sec.android.soagent

null

NSDSWebApp
com.sec.vsim.ericssonnsds.webapp

null

Knox Enrollment Service
com.sec.enterprise.knox.cloudmdm.smdms

null

ConnectivityOverlay
com.samsung.android.ConnectivityOverlay

null

Android Auto
com.google.android.projection.gearhead

null
com.sec.phone
com.sec.phone

null

SecureElementApplication
com.android.se

null

ProxyHandler
com.android.proxyhandler

null

Sim App Dialog
com.android.simappdialog

null

TetheringAutomation
com.sec.automation

null

Wi-Fi Calling
com.sec.unifiedwfc

null

Device Services
com.samsung.android.kgclient

null

iaft
com.sec.android.iaft

null

Android Services Library
com.google.android.ext.services

null

BrightnessBNR
com.samsung.android.brightnessbackupservice

null

Bluetooth
com.android.bluetooth

null

SecVideoEngineService
com.sec.sve

null

Galaxy Store
com.sec.android.app.samsungapps
com.sec.android.app.samsungapps.SamsungAppsMainActivity

DckTimeSyncApplication
com.samsung.android.dck.timesync

null
com.samsung.android.biometrics.app.setting
com.samsung.android.biometrics.app.setting

null

DiagMonAgent
com.sec.android.diagmonagent

null

Main components
com.google.mainline.adservices

null

slocation
com.samsung.android.location

null

Configuration update
com.samsung.android.cidmanager

null

KLMS Agent
com.samsung.klmsagent

null

Service provider location
com.sec.location.nfwlocationprivacy

null

System Tracing
com.android.traceur

null

Accessibility
com.samsung.accessibility

null

Phone
com.samsung.crane

null

SKMSAgentService
com.skms.android.agent

null

ConfigUpdater
com.google.android.configupdater

null

Dynamic System Updates
com.android.dynsystem

null

HTML Viewer
com.android.htmlviewer

null

Game Optimizing Service
com.samsung.android.game.gos

null
com.android.ons
com.android.ons

null

Galaxy Themes
com.samsung.android.themestore

null

Gestural Navigation Bar
com.samsung.internal.systemui.navbar.sec_gestural_no_hint

null
com.samsung.android.wifi.p2paware.resources
com.samsung.android.wifi.p2paware.resources

null

Samsung setup wizard
com.sec.android.app.SecSetupWizard

null

Clipboard edge
com.samsung.android.app.clipboardedge

null

Nearby device scanning
com.samsung.android.beaconmanager

null

Package installer
com.google.android.packageinstaller

null

OsuLogin
com.android.hotspot2.osulogin

null

Gestural Navigation Bar
com.samsung.internal.systemui.navbar.sec_gestural

null

CMHProvider
com.samsung.cmh

null

Galaxy Resource Updater
com.samsung.android.gru

null

Samsung text-to-speech engine
com.samsung.SMT

null

Samsung News
com.samsung.android.app.spage

null

ChromeCustomizations
com.sec.android.app.chromecustomizations

null

Photo Screensavers
com.android.dreams.phototable

null
com.samsung.android.smartswitchassistant
com.samsung.android.smartswitchassistant

null

Smart Call
com.samsung.android.smartcallprovider

null

DeviceKeystring
com.sec.android.app.factorykeystring

null
com.samsung.android.wallpaper.res
com.samsung.android.wallpaper.res

null

System Wi-Fi Resources
com.android.wifi.resources

null
com.android.sharedstoragebackup
com.android.sharedstoragebackup

null

Clock
com.sec.android.app.clockpackage
com.sec.android.app.clockpackage.ClockPackage
com.google.android.sdksandbox
com.google.android.sdksandbox

null

VpnDialogs
com.android.vpndialogs

null

Google Services Framework
com.google.android.gsf

null

Maps
com.google.android.apps.maps
com.google.android.maps.MapsActivity

Weather
com.sec.android.daemonapp

null

Meet
com.google.android.apps.tachyon

null

Corner cutout
com.android.internal.display.cutout.emulation.corner

null

Main components
com.google.android.modulemetadata

null

Bluetooth Agent
com.sec.android.app.bluetoothagent

null

Messages
com.google.android.apps.messaging

null

Contacts
com.samsung.android.app.contacts
com.samsung.android.contacts.contactslist.PeopleActivity

Sticker Center
com.samsung.android.stickercenter

null

Google
com.google.android.googlequicksearchbox
com.google.android.googlequicksearchbox.SearchActivity

Settings Storage
com.android.providers.settings

null

System UI
com.android.systemui

null

Default Print Service
com.android.bips

null

Finder
com.samsung.android.app.galaxyfinder

null
com.google.android.networkstack.tethering.overlay
com.google.android.networkstack.tethering.overlay

null

OneDrive
com.microsoft.skydrive
com.microsoft.skydrive.MainActivity

Permission controller
com.google.android.permissioncontroller

null

IMS Settings
com.samsung.advp.imssettings

null

Sec Media Storage
com.samsung.android.providers.media

null
com.google.android.appsearch.apk
com.google.android.appsearch.apk

null

Media and devices
com.samsung.android.mdx.quickboard

null

Files
com.google.android.documentsui

null

Modes and Routines
com.samsung.android.app.routines

null

Launcher
com.sec.android.emergencylauncher

null
com.google.android.overlay.modules.cellbroadcastservice
com.google.android.overlay.modules.cellbroadcastservice

null

Customization Service
com.samsung.android.rubin.app

null

Network manager
com.google.android.networkstack

null

Samsung account
com.osp.app.signin

null
com.android.backupconfirm
com.android.backupconfirm

null

Google One Time Init
com.google.android.onetimeinitializer

null
com.sprd.wifi.resources.overlay
com.sprd.wifi.resources.overlay

null

Gallery
com.sec.android.gallery3d
com.samsung.android.gallery.app.activity.GalleryActivity
com.samsung.android.networkstack.tethering.overlay
com.samsung.android.networkstack.tethering.overlay

null

Samsung Device Health Manager Service
com.sec.android.sdhms

null

Edge panels
com.samsung.android.app.cocktailbarservice

null

Radio
com.sec.android.app.fm
com.sec.android.app.fm.MainActivity

Settings
com.android.settings
com.android.settings.Settings

Wi-Fi Direct
com.samsung.android.allshare.service.fileshare

null

Gallery stories
com.samsung.storyservice

null

Device Health Services
com.google.android.apps.turbo

null
com.google.android.overlay.modules.permissioncontroller
com.google.android.overlay.modules.permissioncontroller

null

Android Setup
com.google.android.setupwizard

null

Noto Serif / Source Sans Pro
com.android.theme.font.notoserifsource

null

Samsung Editing Assets
com.sec.android.app.ve.vebgm

null

Messages
com.samsung.android.messaging
com.android.mms.ui.ConversationComposer
com.samsung.android.wifi.softapwpathree.resources
com.samsung.android.wifi.softapwpathree.resources

null

Phone services
com.android.phone

null

Android S Easter Egg
com.android.egg

null

MmsService
com.android.mms.service

null

USBSettings
com.sec.usbsettings

null

Eye comfort shield
com.samsung.android.bluelightfilter

null

BadgeProvider
com.sec.android.provider.badge

null

Input Devices
com.android.inputdevices

null

Call Log Backup/Restore
com.android.calllogbackup

null
com.android.providers.partnerbookmarks
com.android.providers.partnerbookmarks

null

Emergency sharing
com.sec.android.app.safetyassurance

null

Google Calendar Sync
com.google.android.syncadapters.calendar

null

Calendar storage
com.android.providers.calendar

null

Captive Portal Login
com.google.android.captiveportallogin

null

Punch Hole cutout
com.android.internal.display.cutout.emulation.hole

null

Sound picker
com.samsung.android.app.soundpicker

null
com.google.android.overlay.gmsconfig.common
com.google.android.overlay.gmsconfig.common

null

TalkBack
com.samsung.android.accessibility.talkback

null

ConnectivityUxOverlay
com.samsung.android.ConnectivityUxOverlay

null

Google Play Store
com.android.vending
com.android.vending.AssetBrowserActivity

Phone calls
com.android.server.telecom

null

Wallpaper services
com.samsung.android.dynamiclock

null
com.android.wallpaperbackup
com.android.wallpaperbackup

null

Chrome
com.android.chrome
com.google.android.apps.chrome.Main
com.android.providers.media
com.android.providers.media

null

SamSungStickerSource
com.src.android.app.camera.sticker

null

SIM toolkit
com.android.stk

null

Family Link parental controls
com.google.android.gms.supervision

null

YouTube
com.google.android.youtube
com.google.android.youtube.app.honeycomb.Shell$HomeActivity

ConfigAPK

android.autoinstalls.config.samsung

null

3 Button Navigation Bar
com.android.internal.systemui.navbar.threebutton

null

Call settings
com.samsung.android.app.telephonyui

null

Dual Messenger
com.samsung.android.da.daagent

null
com.android.wallpapercropper
com.android.wallpapercropper

null

AppCloud
com.aura.oobe.samsung.gl

null

SecSoundPicker
com.samsung.android.secsoundpicker

null

Phone
com.samsung.android.dialer
com.samsung.android.dialer.DialtactsActivity

Samsung Location SDK
com.sec.location.nsflp2

null

MDMApp
com.samsung.android.mdm

null

Separate app sound
com.samsung.android.setting.multisound

null

Clock style
com.samsung.android.app.clockpack

null

Recommended apps
com.samsung.android.app.omcagent

null

Tools
com.sec.android.app.quicktool

null

Certificate installer
com.android.certinstaller

null

Automation Test
com.sec.android.app.DataCreate

null

ImsLogger
com.sec.imslogger

null

MTP application
com.samsung.android.mtp

null

Permission usage
com.samsung.android.privacydashboard

null

NetworkStackOverlay
com.samsung.android.networkstack

null
com.google.android.overlay.gmsconfig.photos
com.google.android.overlay.gmsconfig.photos

null

Download Manager
com.android.providers.downloads

null

Nearby device scanning
com.samsung.android.easysetup

null

Media picker
com.google.android.providers.media.module

null

Configuration update
com.samsung.android.sdm.config

null

Foundation
com.monotype.android.font.foundation

null

Samsung Kids Installer
com.samsung.android.kidsinstaller

null

Tall cutout
com.android.internal.display.cutout.emulation.tall

null
com.google.android.overlay.modules.modulemetadata.forframework
com.google.android.overlay.modules.modulemetadata.forframework

null

DRParser Mode
com.sec.android.app.parser

null
com.android.cts.priv.ctsshim
com.android.cts.priv.ctsshim

null

Sound quality and effects
com.sec.android.app.soundalive

null
com.google.android.overlay.modules.ext.services
com.google.android.overlay.modules.ext.services

null

Downloads
com.android.providers.downloads.ui

null

Blocked Numbers Storage
com.android.providers.blockednumber

null

EasyOneHand
com.sec.android.easyonehand

null

Gestural Navigation Bar
com.android.internal.systemui.navbar.gestural

null

android.auto_generated_rro_product__

android.auto_generated_rro_product__

null

Gallery
com.samsung.android.widget.pictureframe

null

Gmail
com.google.android.gm
com.google.android.gm.ConversationListActivityGmail

Ultra data saving mode
com.samsung.android.uds

null

HandwritingService
com.samsung.android.sdk.handwriting

null

ShortcutBNR
com.samsung.android.shortcutbackupservice

null

Wearable Manager Installer
com.samsung.android.app.watchmanagerstub

null

Digital Wellbeing
com.samsung.android.forest

null

WcmUrlsNetworkStackOverlay
com.samsung.android.wcmurlsnetworkstack

null

Google Wi-Fi Provisioner
com.google.android.apps.carrier.carrierwifi

null

CameraExtensionsProxy
com.android.cameraextensions

null
"""

all_line = text.splitlines()
# print(all_line)

for lines in all_line:
    if not lines.startswith("com."):
        formatted_text += "\n"
    
    formatted_text += f"\n{lines}"
print(formatted_text)

# after you build formatted_text
with open(r"C:\Users\Wei Jie\AppData\Local\Python\apps_list.txt", "w", encoding="utf-8") as f:
    f.write(formatted_text)

