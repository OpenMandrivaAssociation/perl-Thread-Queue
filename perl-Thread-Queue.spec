
%define realname   Thread-Queue
%define version    2.11
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Thread-safe queues
Source:     http://www.cpan.org/modules/by-module/Thread/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Thread::Semaphore)
BuildRequires: perl(threads::shared)

BuildArch: noarch

%description
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.

Any data types supported by the threads::shared manpage can be passed via
queues:

* Ordinary scalars

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


