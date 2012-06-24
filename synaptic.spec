Summary:	WINGs based graphical front-end for APT
Summary(pt_BR):	Front-end gr�fico para APT baseado em WINGs
Summary(es):	Front-end grafico para APT
Summary(pl):	Bazuj�cy na WING graficzny interfejs do APTa
Name:		synaptic
Version:	0.16
Release:	1
URL:		http://distro.conectiva.com/projetos/46/
Source0:	ftp://ftp.conectiva.com/pub/conectiva/EXPERIMENTAL/synaptic/%{name}-%{version}.tar.gz
License:	GPL
Group:		Applications/Archiving
BuildRequires:	apt-devel >= 0.3.19cnc36
BuildRequires:	WindowMaker-devel >= 0.65.0
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Synaptic is a graphical front-end for APT (Advanced Package Tool)
written with the Window Maker toolkit. It attempts to be a lot easier
to use than other existing APT front-ends.

Instead of using trees to display packages, Synaptic is heavily based
on a powerful package filtering system. That greatly simplifies the
interface while giving a lot more flexibility to browse through very
long package lists.

%description -l es
Synaptic is a graphical front-end for APT (Advanced Package Tool)
written with the Window Maker toolkit. It attempts to be a lot easier
to use than other existing APT front-ends.

Instead of using trees to display packages, Synaptic is heavily based
on a powerful package filtering system. That greatly simplifies the
interface while giving a lot more flexibility to browse through very
long package lists.

%description -l pt_BR
Synaptic � um front-end gr�fico para o APT (Advanced Package Tool)
escrito com o toolkit do Window Maker. Seu objetivo � ser mais f�cil
de usar que outros front-ends do APT.

Em vez de utilizar estruturas em �rvore para mostrar os pacotes,
Synaptic utiliza um sistema de filtro de pacotes, simplificando a
interface e oferecendo mais flexibilidade quando houver um grande
numero de pacotes listado.

%description -l pl
Synaptic jest graficznym frontendem dla APT napisany z u�yciem
toolkita WindowMakera. Synaptic pr�buje by� �atwiejszym w u�yciu ni�
inne istniej�ce frontendy dla APT.

Zamiast u�ywaj�c drzew do wy�wietlania pakiet�w, Synaptic mocno bazuje
na systemie filtrowania pakiet�w o ogromnych mo�liwo�ciach. To w
ogromnym stopniu upraszcza interfejs r�wnocze�nie daj�c znacznie
wi�ksz� elastyczno�� podczas przegl�dania d�ugich list pakiet�w.

%prep
%setup -q

%build
%configure2_13
%{__make}

gzip -9nf AUTHORS INSTALL NEWS COPYING README TODO %{name}-hackers-guide.txt

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
install -d %{buildroot}%{_localstatedir}/lib/%{name}/
install -D -m755 src/%{name} %{buildroot}/%{_bindir}/%{name}
install -D help.txt %{buildroot}%{_datadir}/%{name}/help.txt
install -D %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
(cd po;make install prefix=%{buildroot}/%{_prefix})
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/help.txt
%{_localstatedir}/lib/%{name}
%doc AUTHORS.gz INSTALL.gz NEWS.gz COPYING.gz
%doc README.gz TODO.gz %{name}-hackers-guide.txt.gz
