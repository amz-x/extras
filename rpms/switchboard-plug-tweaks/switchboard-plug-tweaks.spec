%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type personal
%global plug_name pantheon-tweaks

Name:           switchboard-plug-tweaks
Summary:        Switchboard Tweaks Plug 
Version:        1.0.3
Release:        %autorelease
License:        GPLv3+

URL:            https://github.com/pantheon-tweaks/pantheon-tweaks
Source0:        %{url}/archive/%{version}/%{plug_name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       hicolor-icon-theme

%description
A system settings panel for the Pantheon Desktop Environment that lets
you easily and safely customise your desktop's appearance.

%prep
%autosetup -n %{plug_name}-%{version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_name}.appdata.xml

%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_name}.appdata.xml


%files -f %{plug_name}-plug.lang
%license COPYING
%doc README.md

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_name}.appdata.xml
%{_datadir}/icons/hicolor/*/categories/preferences-*.svg


%changelog
%autochangelog