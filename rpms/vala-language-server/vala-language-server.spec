%global srcname %{name}-alpha

%global build_version 1
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global build_name %{srcname}-%{build_timestamp}-%{build_version}

Name:           vala-language-server
Version:        %{build_timestamp}
Release:        %{build_version}%{?dist}
Summary:        Vala Language Server

License:        GPLv2+
URL:            https://github.com/philippejer/%{srcname}
Source0:        https://github.com/philippejer/%{srcname}/archive/master.tar.gz#/%{build_name}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-devel

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0)

%description
%{summary}.

%prep
%autosetup -n %{srcname}-master

%build
%meson
%meson_build

%install
mkdir -p "%{buildroot}/usr/bin"
install -m 0755 "x86_64-redhat-linux-gnu/%{name}" "%{buildroot}/usr/bin/%{name}"

%files
%{_bindir}/%{name}

%license LICENSE
%doc README.md

%changelog

* Thu Jan 02 2020 Christopher Crouse <mail@amz-x.com>
- Initialized spec file