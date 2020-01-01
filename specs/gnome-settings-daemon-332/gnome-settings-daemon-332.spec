%global glib2_version 2.56
%global geocode_glib_version 3.10.0
%global gnome_desktop_version 3.27.90
%global gsettings_desktop_schemas_version 3.27.90
%global gtk3_version 3.15.3
%global libgweather_version 3.9.5
%global geoclue_version 2.3.1

%global src_name gnome-settings-daemon

Name:           gnome-settings-daemon-332
Version:        3.32.1
Release:        1%{?dist}
Summary:        The daemon sharing settings from GNOME to GTK+/KDE applications

License:        GPLv2+
URL:            https://download.gnome.org/sources/%{src_name}
Source0:        https://download.gnome.org/sources/%{src_name}/3.32/%{src_name}-%{version}.tar.xz
# Source1:        org.gnome.settings-daemon.plugins.power.gschema.override

BuildRequires:  meson >= 0.44.0
BuildRequires:  gcc
BuildRequires:  cups-devel
BuildRequires:  gettext
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(colord) >= 1.0.2
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(geoclue-2.0) >= %{geoclue_version}
BuildRequires:  pkgconfig(geocode-glib-1.0) >= %{geocode_glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gweather-3.0) >= %{libgweather_version}
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(wayland-client)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libwacom) >= 0.7
BuildRequires:  pkgconfig(xorg-wacom)
%endif

Requires: colord
Requires: iio-sensor-proxy
Requires: geoclue2 >= %{geoclue_version}
Requires: geocode-glib%{?_isa} >= %{geocode_glib_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libgweather%{?_isa} >= %{libgweather_version}

Obsoletes: %{src_name}-updates < 3.13.1
Obsoletes: drwright < 3.5.0-3
Obsoletes: gnome-settings-daemon-devel < 3.23.1

# The "org.gnome.SettingsDaemon.A11yKeyboard" has been been removed, now
# handled in gnome-shell/mutter instead; this conflict here makes sure not to
# break older gdm and gnome-session releases that expect the functionality
Conflicts: gdm < 1:3.27.90
Conflicts: gnome-session < 3.27.90
# The orientation and xrandr plugins were removed in 3.25.4 and their
# functionality was moved to mutter; this conflict here makes sure not to break
# older gdm, gnome-session and gnome-shell releases that expect the functionality
Conflicts: gnome-shell < 3.25.4

%description
A daemon to share settings from GNOME to other applications. It also
handles global keybindings, as well as a number of desktop-wide settings.

%package        devel
Summary:        Development files for %{src_name}
Requires:       %{src_name}%{?_isa} = %{version}-%{release}

%description    devel
The %{src_name}-devel package contains libraries and header files for
developing applications that use %{src_name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

%find_lang %{src_name} --with-gnome

mkdir $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%files -f %{src_name}.lang
%license COPYING
%doc AUTHORS NEWS

# list daemons explicitly, so we notice if one goes missing
# some of these don't have a separate gschema
%{_libexecdir}/gsd-clipboard
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Clipboard.desktop

%{_libexecdir}/gsd-datetime
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop

%{_libexecdir}/gsd-dummy

%{_libexecdir}/gsd-housekeeping
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.housekeeping.gschema.xml

%{_libexecdir}/gsd-keyboard
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop

%{_libexecdir}/gsd-media-keys
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.media-keys.gschema.xml

%{_libexecdir}/gsd-mouse
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Mouse.desktop
%{_libexecdir}/gsd-locate-pointer

%{_libexecdir}/gsd-backlight-helper
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%{_libexecdir}/gsd-power
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.xml
# %{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.override

%{_libexecdir}/gsd-print-notifications
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
%{_libexecdir}/gsd-printer

%{_libexecdir}/gsd-rfkill
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop

%{_libexecdir}/gsd-screensaver-proxy
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop

%{_libexecdir}/gsd-smartcard
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop

%{_libexecdir}/gsd-sound
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop

%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.wacom.gschema.xml
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop

%ifnarch s390 s390x
%{_libexecdir}/gsd-wacom
%{_libexecdir}/gsd-wacom-led-helper
%{_libexecdir}/gsd-wacom-oled-helper
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%endif

%{_libexecdir}/gsd-xsettings
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xsettings.gschema.xml

%{_libexecdir}/gsd-a11y-settings
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop

%{_libexecdir}/gsd-color
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.color.gschema.xml

%{_libexecdir}/gsd-sharing
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.sharing.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/libgsd.so

/usr/lib/udev/rules.d/*.rules
%{_datadir}/gnome-settings-daemon/
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert

%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gschema.xml

%files devel
%{_includedir}/gnome-settings-daemon-3.0
%{_libdir}/pkgconfig/gnome-settings-daemon.pc

%changelog
* Wed Jan 01 2020 Christopher Crouse <mail@amz-x.com> - 3.32.1
- Update to 3.34.2