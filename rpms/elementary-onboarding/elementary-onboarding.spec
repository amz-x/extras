%define srcname onboarding
%define appname io.elementary.onboarding

Name:           elementary-onboarding
Version:        6.1.0
Release:        2%{?dist}
Summary:        Onboarding app for new users

License:        GPLv3+
URL:            https://github.com/elementary/onboarding
Source0:        https://github.com/elementary/onboarding/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Patch to rename mo.po to ro_MD.po in language files to show no errors in rpmlint results
Patch0:         https://patch-diff.githubusercontent.com/raw/elementary/onboarding/pull/151.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)     >= 2.64.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)      >= 5.5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)   >= 0.80.0

%description
%{summary}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{appname}

%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml

%files -f %{appname}.lang

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg

%config(noreplace) /etc/xdg/autostart/*
%config /etc/xdg/autostart/%{appname}.desktop

%doc README.md
%license COPYING

%changelog

* Fri Dec 17 2021 Christopher Crouse <mail@amz-x.com>
- 6.1.0-2
- Included patch to language files

* Fri Dec 17 2021 Christopher Crouse <mail@amz-x.com>
- 6.1.0-1
- Initialized spec file