Name:		texlive-sort-by-letters
Version:	27128
Release:	2
Summary:	Bibliography styles for alphabetic sorting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/sort-by-letters
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains several bibliography styles for separating
a document's references by the first letter of the first
author/editor in the bibliography entry. The styles are adapted
from standard ones or from natbib ones.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/sort-by-letters/abbrv-letters.bst
%{_texmfdistdir}/bibtex/bst/sort-by-letters/alpha-letters.bst
%{_texmfdistdir}/bibtex/bst/sort-by-letters/apalike-letters.bst
%{_texmfdistdir}/bibtex/bst/sort-by-letters/frplainnat-letters.bst
%{_texmfdistdir}/bibtex/bst/sort-by-letters/plain-letters.bst
%{_texmfdistdir}/bibtex/bst/sort-by-letters/plainnat-letters.bst
%{_texmfdistdir}/bibtex/bst/sort-by-letters/siam-letters.bst
%doc %{_texmfdistdir}/doc/bibtex/sort-by-letters/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
