#
# Conditional build:
%bcond_with	tests		# perform "make test"
				# Text::TabularDisplay 1.21 not available yet
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	RecordParser
Summary:	Text::RecordParser - read record-oriented files
Summary(pl):	Text::RecordParser - odczyt plików rekordowych
Name:		perl-Text-RecordParser
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	db2490a5548247da8d393f945d9a245e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-TabularDisplay >= 1.21
BuildConflicts:	perl-Text-TabularDisplay = 1.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is for reading record-oriented data. The most common
example have records separated by newlines and fields separated by
commas or tabs, but this module aims to provide a consistent interface
for handling sequential records in a file however they may be
delimited. Typically this data lists the fields in the first line of
the file, in which case you should call bind_header to bind the field
name. If the first line contains data, you can still bind your own
field names via bind_fields. Either way, you can then use many methods
to get at the data as arrays or hashes.

%description -l pl
Ten modu³ s³u¿y do czytania danych zorientowanych rekordowo.
Najpopularniejszy przyk³ad to rekordy oddzielone nowymi liniami i pola
oddzielone przecinkami lub tabulatorami, ale celem tego modu³u jest
dostarczenie spójnego interfejsu do obs³ugi sekwencyjnych rekordów w
pliku niezale¿nie od sposobu ich rozdzielenia. Typowo dane te
okre¶laj± pola w pierwszej linii pliku - w tym przypadku nale¿y
wywo³aæ bind_header aby podpi±æ nazwy pól. Je¶li pierwsza linia
zawiera dane, nadal mo¿na podpi±æ w³asne nazwy pól poprzez
bind_fields. W ka¿dym przypadku mo¿na potem u¿ywaæ wielu metod
pobierania danych jako tablice lub hasze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Text/*.pm
%{_mandir}/man?/*
