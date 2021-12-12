%define debug_package %{nil}

Name:           rbenv
Version:        1.2.0
Release:        1%{?dist}
Summary:        Simple ruby version manager

BuildArch:      noarch
License:        MIT
URL:            https://github.com/rbenv/rbenv
Source0:        https://github.com/rbenv/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%install

mkdir -p "%{buildroot}/usr/bin"
mkdir -p "%{buildroot}/usr/share/doc/%{name}"
mkdir -p "%{buildroot}/usr/share/licenses/%{name}"
mkdir -p "%{buildroot}/usr/lib/%{name}/completions"
mkdir -p "%{buildroot}/usr/lib/%{name}/libexec"

install -m 644 completions/*            "%{buildroot}/usr/lib/%{name}/completions/"
install -m 755 libexec/*                "%{buildroot}/usr/lib/%{name}/libexec/"

ln -s /usr/lib/%{name}/libexec/%{name}  "%{buildroot}/usr/bin/"

%files

%{_bindir}/%{name}

/usr/lib/%{name}/completions/*
/usr/lib/%{name}/libexec/*

%license LICENSE
%doc README.md

%changelog

* Sun Dec 12 2021 Christopher Crouse <mail@amz-x.com>
- Init spec