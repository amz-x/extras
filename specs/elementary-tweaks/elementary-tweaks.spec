%global srcname %{name}-master
%global plugname %{name}-plug
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}

Name:           elementary-tweaks
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A system settings panel for elementary

License:        GPLv3+   
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/master.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires: 	pkgconfig(switchboard-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{srcname}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plugname}

%files -f %{plugname}.lang
%license COPYING
%doc README.md

%{_libdir}/switchboard/personal/lib%{name}.so

%{_datadir}/icons/hicolor/*/categories/preferences-*.svg

%changelog
* Mon Apr 22 2019 Christopher Crouse <amz.x@protonmail.com>
- Initialized spec file
