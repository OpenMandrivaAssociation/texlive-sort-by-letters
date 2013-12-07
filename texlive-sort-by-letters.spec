# revision 27128
# category Package
# catalog-ctan /biblio/bibtex/contrib/sort-by-letters
# catalog-date 2012-06-04 23:25:44 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-sort-by-letters
Version:	20120604
Release:	3
Summary:	Bibliography styles for alphabetic sorting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/sort-by-letters
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120604-1
+ Revision: 812878
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070312-2
+ Revision: 756074
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070312-1
+ Revision: 719556
- texlive-sort-by-letters
- texlive-sort-by-letters
- texlive-sort-by-letters
- texlive-sort-by-letters

