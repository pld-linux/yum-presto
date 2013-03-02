Summary:	Presto plugin for yum
Name:		yum-presto
Version:	0.9.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.lesbg.com/jdieter/presto/%{name}-%{version}.tar.bz2
# Source0-md5:	1dacbe50b9f941792c915e08ec8093bc
URL:		http://www.lesbg.com/jdieter/presto/
BuildRequires:	python-babel
BuildRequires:	python-distribute
Requires:	deltarpm >= 3.4-2
Requires:	python >= 1:2.4
Requires:	yum >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib/yum-plugins

%description
Yum-presto is a plugin for yum that looks for deltarpms rather than
rpms whenever they are available. This has the potential of saving a
lot of bandwidth when downloading updates.

A Deltarpm is the difference between two rpms. If you already have
foo-1.0 installed and foo-1.1 is available, yum-presto will download
the deltarpm for foo-1.0 => 1.1 rather than the full foo-1.1 rpm, and
then build the full foo-1.1 package from your installed foo-1.0 and
the downloaded deltarpm.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/presto.conf
%{_libexecdir}/presto.py
%{py_sitescriptdir}/yum_presto-*.egg-info
