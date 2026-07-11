%global tl_name sort-by-letters
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bibliography styles for alphabetic sorting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/sort-by-letters
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sort-by-letters.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains several bibliography styles for separating a
document's references by the first letter of the first author/editor in
the bibliography entry. The styles are adapted from standard ones or
from natbib ones.

