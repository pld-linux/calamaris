%include        /usr/lib/rpm/macros.perl
Summary:	Squid and NetCache log parser and report generator
Summary(pl):	Generator raportów dla Squida i NetCache
Name:		calamaris
Version:	2.56
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://Cord.de/tools/squid/calamaris/%{name}-%{version}.tar.gz
Source1:	%{name}.crontab
Source2:	%{name}.sysconfig
Source3:	%{name}-croniface
Requires:	/etc/cron.d
Requires:	crontabs
Requires:	/bin/zcat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calamaris is statistical info generator for Squid and NetCache based
on log parsing. It can create both plain-text and HTML reports. A
must-have for Squid/NetCache administrators.

%description -l pl
Calamaris generuje informacje statystyczne o pracy Squida i NetCache w
oparciu o ich logi. Potrafi tworzyæ raporty w postaci czystego tekstu
jak i HTML. Niezbêdny dla administratorów Squida i NetCache.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{cron.d,sysconfig},%{_bindir},%{_sbindir},%{_mandir}/man1}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/calamaris
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/calamaris
install %{SOURCE3} $RPM_BUILD_ROOT%{_sbindir}
install calamaris $RPM_BUILD_ROOT%{_bindir}
install calamaris.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES EXAMPLES README
%attr(750,root,root) %config(noreplace) /etc/cron.d/calamaris
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/calamaris
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/*/*
