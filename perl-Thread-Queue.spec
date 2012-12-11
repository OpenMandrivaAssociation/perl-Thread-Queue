%define upstream_name    Thread-Queue
%define upstream_version 2.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Thread-safe queues
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Thread/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Thread::Semaphore)
BuildRequires:	perl(threads::shared)
Provides:	perl(Thread::Queue) = %perl_convert_version %{upstream_version}
BuildArch:	noarch

%description
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.

Any data types supported by the threads::shared manpage can be passed via
queues:

* Ordinary scalars

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.120.0-2mdv2011.0
+ Revision: 657854
- rebuild for updated spec-helper

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.120.0-1mdv2011.0
+ Revision: 625283
- update to new version 2.12

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 2.110.0-2mdv2010.0
+ Revision: 410884
- add versioned provides

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.110.0-1mdv2010.0
+ Revision: 401514
- rebuild using %%perl_convert_version
- fixed license field

* Sat Jan 17 2009 Jérôme Quelin <jquelin@mandriva.org> 2.11-1mdv2009.1
+ Revision: 330716
- import perl-Thread-Queue


* Sat Jan 17 2009 cpan2dist 2.11-1mdv
- initial mdv release, generated with cpan2dist

