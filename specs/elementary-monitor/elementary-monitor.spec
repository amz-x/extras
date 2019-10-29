%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname monitor
%global appname com.github.stsdc.monitor

Name:           elementary-monitor
Summary:        Manage processes and monitor system resources
Version:        0.6.0
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/stsdc/%{srcname}
Source0:        https://github.com/stsdc/%{srcname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(wingpanel-2.0)

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstreamcli validate --nonet \
   %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml

%files -f %{appname}.lang

%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_libdir}/wingpanel/lib%{srcname}.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg

%changelog

* Tue Oct 29 2019 Christopher Crouse <mail@amz-x.com>
- Bumped to v0.6.0
- Updated 

* Sat Oct 26 2019 Christopher Crouse <mail@amz-x.com>
- Bumped
- Updated Patch

* Wed Aug 21 2019 Christopher Crouse <mail@amz-x.com>
- Updated patch URL  

* Tue Aug 13 2019 Christopher Crouse <mail@amz-x.com>
- Bumped version 
- Temporary workaround for appstreamcli 

* Mon Apr 22 2019 Christopher Crouse <mail@amz-x.com>
- Updated spec file to use appstreamcli

* Mon Apr 15 2019 Christopher Crouse <mail@amz-x.com> 
- Setup spec