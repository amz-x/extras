%global srcname	aesop
%global appname	com.github.lainsce.aesop

Name:			elementary-pdf-viewer
Version:        1.1.1
Release:        1%{?dist}
Summary:        The simplest PDF viewer around

License:        GPLv3+   
URL:            https://github.com/lainsce/%{srcname}
Source0:        https://github.com/lainsce/%{srcname}/archive/1.1.1.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:	pkgconfig(poppler-glib)

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

%files
%{_bindir}/%{appname}

%changelog
* Mon May 20 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file