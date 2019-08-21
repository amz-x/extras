%define debug_package %{nil}

Name:           devilbox
Version:        1.0.2
Release:        1%{?dist}
Summary:        The Devilbox is a modern and highly customisable dockerized PHP stack supporting full LAMP and MEAN and running on all major platforms

License:        MIT
URL:            https://github.com/getantibody/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p "%{buildroot}/opt/%{name}"
install -m 0755 -d "%{name}" "%{buildroot}/opt/%{name}"

# copy example env
cp -v  "%{buildroot}/opt/%{name}/env-example" "%{buildroot}/opt/%{name}/.env"

# cleanup
rm -vr "%{buildroot}/opt/%{name}/.git"
rm -vr "%{buildroot}/opt/%{name}/.github"

%files
%{_bindir}/%{name}

%license LICENSE.md
%doc README.md

%changelog
* Wed Aug 21 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file
