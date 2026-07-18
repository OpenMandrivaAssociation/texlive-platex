%global tl_name platex
%global tl_revision 77830
%global tl_bin_links platex:euptex platex-dev:euptex

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	pLaTeX2e and miscellaneous macros for pTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/platex
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/platex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/platex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/platex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(firstaid)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(l3backend)
Requires:	texlive(l3backend-dev)
Requires:	texlive(l3kernel)
Requires:	texlive(l3kernel-dev)
Requires:	texlive(latex)
Requires:	texlive(latex-base-dev)
Requires:	texlive(latex-firstaid-dev)
Requires:	texlive(latex-fonts)
Requires:	texlive(platex.bin)
Requires:	texlive(ptex)
Requires:	texlive(ptex-fonts)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Requires:	texlive(uptex)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The bundle provides pLaTeX2e and miscellaneous macros for pTeX and
e-pTeX. This is a community edition forked from the original ASCII
edition (ptex-texmf-2.5).

