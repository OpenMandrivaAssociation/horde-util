%define prj    Util
%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-util
Version:       0.1.0
Release:       4
Summary:       Horde Util package
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      php-mbstring
Requires:      php-iconv
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
These classes provide functionality useful for all kind of applications.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%{peardir}/Horde/Array.php
%{peardir}/Horde/String.php
%{peardir}/Horde/Util.php
%{peardir}/Horde/Variables.php
%dir %{peardir}/tests/Util
%dir %{peardir}/tests/Util/tests
%{peardir}/tests/Util/tests/*.phpt



%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-3mdv2011.0
+ Revision: 564107
- Increased release for rebuild

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-2mdv2010.1
+ Revision: 509336
- increased rel version
- Removed  Requires:horde-browser to break the infinite build loop problem

* Mon Feb 15 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 506036
- replace PreReq with Requires(pre)
- import horde-util


