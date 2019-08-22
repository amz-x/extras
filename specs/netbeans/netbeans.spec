Name:			netbeans
Version:		11.1
Release:		1%{?dist}
Summary:		Apache NetBeans is an open source development environment, tooling platform, and application framework

License:		Apache-2.0
URL:			https://netbeans.org/
Source0:		https://www-eu.apache.org/dist/%{name}/%{name}/%{version}/%{name}-%{version}-bin.zip#/%{name}-%{version}.zip

Requires:		java >= 1:1.8.0
Requires:		java-headless >= 1:1.8.0

%description
%{summary}.

%prep
%autosetup -n %{name}

%install

# copy files
mkdir -p "%{buildroot}/opt/%{name}"
cp -vr "." "%{buildroot}/opt/%{name}"

# python fix
sed -i 's/python/python3/g' "%{buildroot}/opt/%{name}/extide/ant/bin/runant.py"

# cleanup
rm -rf "%{buildroot}/opt/%{name}/ide/bin/nativeexecution/SunOS"*
rm -rf "%{buildroot}/opt/%{name}/ide/bin/nativeexecution/MacOSX"*
rm -rf "%{buildroot}/opt/%{name}/ide/bin/nativeexecution/Windows"*
rm -rf "%{buildroot}/opt/%{name}/ide/bin/nativeexecution/"*-sparc_64
rm -rf "%{buildroot}/opt/%{name}/profiler/lib/deployed/jdk16/solaris-"*
rm -rf "%{buildroot}/opt/%{name}/profiler/lib/deployed/jdk16/hpux-"*
rm -rf "%{buildroot}/opt/%{name}/profiler/lib/deployed/jdk16/linux-arm"*
rm -rf "%{buildroot}/opt/%{name}/profiler/lib/deployed/jdk15/hpux-"*
rm -rf "%{buildroot}/opt/%{name}/profiler/lib/deployed/jdk15/solaris-"*
find "%{buildroot}/opt/%{name}/" -name "*.exe" -exec rm {} \;
find "%{buildroot}/opt/%{name}/" -name "*.dll" -exec rm {} \;

%files
/opt/%{name}

%license LICENSE
%doc README.html

%changelog
* Thu Aug 22 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file
