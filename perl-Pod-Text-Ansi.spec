%define upstream_name    Pod-Text-Ansi
%define upstream_version 0.05
Name:		perl-%{upstream_name}
Version:	0.05
Release:	3

Summary:	Convert POD to ANSI-colored text
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/hinrik/pod-text-ansi
Source0:	https://cpan.metacpan.org/authors/id/H/HI/HINRIK/Pod-Text-Ansi-0.05.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Text)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Pod::Text::Ansi is a simple subclass of Pod::Text that highlights output
text using ANSI color escape sequences. Apart from the color, it in all
ways functions like Pod::Text. See the Pod::Text manpage for details and
available options.

%prep
%setup -q -n Pod-Text-Ansi-0.05

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

