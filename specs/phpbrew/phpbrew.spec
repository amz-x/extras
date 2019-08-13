%define debug_package %{nil}

Name:           phpbrew
Version:        1.23.1
Release:        1%{?dist}
Summary:        Builds and installs multiple version php(s) in your $HOME directory

License:        MIT
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  git

%description
%{summary}.

%prep

%autosetup

%build

%install
mkdir -p "%{buildroot}/usr/bin"
chmod +x %{name}
install -m 0755 "%{name}" "%{buildroot}/usr/bin/%{name}"

%files
%{_bindir}/%{name}

%license LICENSE
%doc README.md

%changelog
* Tue Aug 13 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file