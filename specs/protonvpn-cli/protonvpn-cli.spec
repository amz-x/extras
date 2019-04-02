%define debug_package %{nil}

Name:           protonvpn-cli
Version:        1.1.2
Release:        1%{?dist}
Summary:        ProtonVPN CLI

License:        MIT
URL:            https://github.com/ProtonVPN/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       openvpn
Requires:       python3
Requires:       dialog
Requires:       wget

BuildRequires:  git

%description
ProtonVPN CLI is a command-line tool for Linux and macOS.

%prep

%autosetup

%build

%install
mkdir -p "%{buildroot}/usr/bin"
install -m 0755 "%{name}.sh" "%{buildroot}/usr/bin/%{name}"

%files
%{_bindir}/%{name}

%license license.md
%doc README.md

%changelog
* Mon Apr 1 2019 Christopher Crouse <amz.x@protonmail.com>
- Initialized spec file
