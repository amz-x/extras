%define debug_package %{nil}

%global build_version 1
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global build_name %{name}-%{build_timestamp}-%{build_version}

Name:           wingpanel-indicator-ayatana
Version:        %{build_timestamp}
Release:        %{build_version}%{?dist}
Summary:        Wingpanel Ayatana-Compatibility Indicator (Community Version)

License:        GPLv2+
URL:            https://github.com/Lafydev/wingpanel-indicator-ayatana
Source0:        https://github.com/Lafydev/wingpanel-indicator-ayatana/archive/master.tar.gz#/%{build_name}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0
BuildRequires:  pkgconfig(indicator3-0.4)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
%{summary}.

%prep
%autosetup -n %{name}-master


%build
%meson
%meson_build


%install
%meson_install

%files

%{_libdir}/wingpanel/libayatana.so

%doc README.md
%license COPYING

%changelog

* Wed Jul 14 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file