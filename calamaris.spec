# TODO:
# - think about default directory for calamaris output (somwhere in /var) so
#   it works out-of-the-box
#
Summary:	Squid and NetCache log parser and report generator
Summary(pl.UTF-8):	Generator raportów dla Squida i NetCache
Name:		calamaris
Version:	2.99.4.0
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://cord.de/tools/squid/calamaris/%{name}-%{version}.tar.gz
# Source0-md5:	61d4fe8b4c00550b58dff09b643aff10
Source1:	%{name}.crontab
Source2:	%{name}.sysconfig
Source3:	%{name}-croniface
URL:		http://cord.de/tools/squid/calamaris/Welcome.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	/bin/zcat
Requires:	crondaemon
Requires:	setup >= 2.4.6
Conflicts:	logrotate < 3.7-3
Conflicts:	squid < 7:2.5.STABLE7-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calamaris is statistical info generator for Squid and NetCache based
on log parsing. It can create both plain-text and HTML reports. A
must-have for Squid/NetCache administrators.

%description -l pl.UTF-8
Calamaris generuje informacje statystyczne o pracy Squida i NetCache w
oparciu o ich logi. Potrafi tworzyć raporty w postaci czystego tekstu
jak i HTML-a. Niezbędny dla administratorów Squida i NetCache.

%prep
%setup -q
%{__sed} -i -e 's/use ident/use the ident/' calamaris calamaris.conf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{cron.d,sysconfig},%{_bindir},%{_sbindir},%{_mandir}/man1}

install -p %{SOURCE3} $RPM_BUILD_ROOT%{_sbindir}
install -p calamaris $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/calamaris
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/calamaris
cp -p calamaris.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES EXAMPLES README
%config(noreplace) /etc/cron.d/calamaris
%attr(640,root,stats) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/calamaris
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/*/*
