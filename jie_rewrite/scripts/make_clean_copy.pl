#!/usr/bin/perl
use strict;
use warnings;
use utf8;
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# Usage: perl make_clean_copy.pl <src_dev_file> <dest_published_file>
my ($src, $dst) = @ARGV;
die "usage: make_clean_copy.pl <src> <dst>\n" unless $src && $dst;

open(my $fh, "<:encoding(UTF-8)", $src) or die "cannot open $src: $!";
my @lines = <$fh>;
close($fh);
chomp(@lines);

die "$src: empty file\n" unless @lines;
$lines[0] =~ s/^\x{FEFF}//;
die "$src: first line is not a title (# ...): $lines[0]\n" unless $lines[0] =~ /^#\s/;

my $title = $lines[0];

# find start of prose: skip blank lines and metadata lines (starting with '>') after title
my $i = 1;
while ($i < @lines) {
    my $l = $lines[$i];
    if ($l =~ /^\s*$/ || $l =~ /^>/) {
        $i++;
        next;
    }
    last;
}
my $prose_start = $i;

# find footer separator: last line that is exactly '---' whose next non-blank line starts with '## '
my $footer_idx = -1;
for (my $j = 0; $j < @lines; $j++) {
    if ($lines[$j] =~ /^---\s*$/) {
        my $k = $j + 1;
        $k++ while ($k < @lines && $lines[$k] =~ /^\s*$/);
        if ($k < @lines && $lines[$k] =~ /^##\s/) {
            $footer_idx = $j;
        }
    }
}

my $prose_end;
if ($footer_idx >= 0) {
    $prose_end = $footer_idx - 1;
} else {
    $prose_end = $#lines;
}

# trim trailing blank lines from prose_end
while ($prose_end >= $prose_start && $lines[$prose_end] =~ /^\s*$/) {
    $prose_end--;
}

my @prose = @lines[$prose_start .. $prose_end];

# match existing published/ convention: CRLF line endings, no BOM, no trailing blank line beyond one final CRLF
open(my $out, ">:raw:encoding(UTF-8)", $dst) or die "cannot open $dst for writing: $!";
print $out "$title\r\n\r\n";
print $out join("\r\n", @prose), "\r\n";
close($out);

print "OK: $dst (title-only heading kept; prose lines: " . scalar(@prose) . "; footer stripped: " . ($footer_idx >= 0 ? "yes" : "NO FOOTER FOUND") . ")\n";
