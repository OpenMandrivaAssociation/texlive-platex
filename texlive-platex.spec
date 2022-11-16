Name:		texlive-platex
Version:	64072
Release:	1
Summary:	pLaTeX2e and miscellaneous macros for pTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/platex
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides pLaTeX2e and miscellaneous macros for pTeX
and e-pTeX. This is a community edition forked from the
original ASCII edition (ptex-texmf-2.5).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/platex
%{_texmfdistdir}/texmf-dist/tex/platex
%doc %{_texmfdistdir}/texmf-dist/doc/platex
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/platex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/platex.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
