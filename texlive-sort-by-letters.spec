# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/sort-by-letters
# catalog-date 2007-03-12 11:51:09 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-sort-by-letters
Version:	20070312
Release:	1
Summary:	Bibliography styles for alphabetic sorting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/sort-by-letters
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This bundle contains several bibliography styles for separating
a document's references by the first letter of the first
author/editor in the bibliography entry. The styles are adapted
from standard ones or from natbib ones.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_texmfdistdir}/doc/latex/sort-by-letters/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
