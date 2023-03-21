from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import *
 
class KqlLexer(RegexLexer):
    name = 'Kusto/KQL'
    aliases = ['kql', 'kusto']
    filenames = ['*.kql', '*.kusto']
    flags = re.MULTILINE | re.DOTALL
 
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'//.*?$', Comment.Single),
            (words(('let', 'where', 'join', 'on', 'and', 'or', 'not', 'contains', 'startswith', 'endswith'), suffix=r'\b'), Operator.Word),
            (words(('datatable', 'union', 'project', 'extend', 'mv-expand', 'parse', 'summarize', 'where', 'join', 'hint', 'as', 'with', 'typeof', 'iffalse', 'case', 'coalesce', 'isempty', 'isnotempty', 'pack', 'todynamic', 'toscalar', 'toupper', 'tolower', 'trim', 'substring', 'replace', 'regex', 'exp', 'log', 'power', 'sqrt', 'floor', 'ceiling', 'round', 'rand', 'todatetime', 'time', 'datetime', 'now', 'ago', 'startofday', 'endofday', 'startofweek', 'endofweek', 'startofmonth', 'endofmonth', 'startofyear', 'endofyear', 'array_length', 'array_concat', 'array_slice', 'array_sort', 'array_reverse', 'array_indexof', 'array_contains', 'array_sum', 'array_agg', 'tostring', 'parse_json', 'toarray', 'tosingle', 'totimespan', 'tolong', 'toint', 'todynamic'), suffix=r'\b'), Name.Function),
            (r'(\<)(\w+)(\>)', bygroups(Punctuation, Name.Class, Punctuation)),
            (r'@[\w\.]+', Name.Variable),
            (r'\w+\.\w+', Name.Namespace),
            (r"'([^'\\]|\\.)*'", String.Single),
            (r'"([^"\\]|\\.)*"', String.Double),
            (r'[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?', Number.Float),
            (r'[+-]?\d+', Number.Integer),
            (r'[^\W\d]\w*', Name),
            (r'(\{|\}|\(|\)|\[|\])', Punctuation),
            (r'[,;:=]', Punctuation),
            (r'.', Text),
        ],
    }
