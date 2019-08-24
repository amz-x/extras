# Issue building from source:
# https://issues.apache.org/jira/browse/NETBEANS-239 

%global __provides_exclude_from ^.*\\.so$

Name:			netbeans
Version:		11.1
Release:		1%{?dist}
Summary:		Apache NetBeans is an open source development environment, tooling platform, and application framework

License:		Apache-2.0
URL:			https://netbeans.org/
Source0:		https://www-eu.apache.org/dist/%{name}/%{name}/%{version}/%{name}-%{version}-bin.zip#/%{name}-%{version}.zip
Source1:		https://gitlab.com/amz-x/extras/blob/master/sources/%{name}/%{name}.desktop

Requires:		java >= 1:1.8.0
Requires:		java-devel >= 1:1.8.0
Requires:		java-headless >= 1:1.8.0

%description
%{summary}.

%prep
%autosetup -n %{name}

# @TODO - Need to replace _sourcedir
cp -v "%{_sourcedir}/%{name}.desktop" "%{_builddir}/%{name}/%{name}.desktop"

%install

mkdir -p "%{buildroot}%{_bindir}"
mkdir -p "%{buildroot}%{_datadir}/applications"
mkdir -p "%{buildroot}/opt/%{name}"

cp -vr "." "%{buildroot}/opt/%{name}"

# cli
ln -s "/opt/%{name}/bin/%{name}" "%{buildroot}%{_bindir}/%{name}"

# desktop
cp -v "%{name}.desktop" "%{buildroot}%{_datadir}/applications/%{name}.desktop"

# python fix
sed -i 's/python/python3/g' "%{buildroot}/opt/%{name}/extide/ant/bin/runant.py"

# cleanup
rm -r "%{buildroot}/opt/%{name}/%{name}.desktop"
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

%{_bindir}/%{name}

%{_datadir}/applications/%{name}.desktop

%license LICENSE
%doc README.html

%changelog
* Sat Aug 24 2019 Christopher Crouse <mail@amz-x.com>
- Updated spec file

* Thu Aug 22 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file
