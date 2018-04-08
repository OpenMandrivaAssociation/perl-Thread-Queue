%define upstream_name    Thread-Queue
%define upstream_version 3.12
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Thread-safe queues
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Thread/Thread-Queue-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Thread::Semaphore)
BuildRequires:	perl(threads::shared)
BuildArch:	noarch

%description
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.

Any data types supported by the threads::shared manpage can be passed via
queues:

* Ordinary scalars

%prep
%autosetup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
