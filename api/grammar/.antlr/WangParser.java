// Generated from d:\Luis Alonso\Material Universitario\2018\II Semestre\Paradigmas de Programación\10 Proyectos\P1\wang_python\servidor_django\api\grammar\Wang.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class WangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, COMMA=3, DOT=4, LEADSTO=5, NOT=6, AND=7, OR=8, IMPLIES=9, 
		BICONDITIONAL=10, ID=11, WS=12, ErrorChar=13;
	public static final int
		RULE_deduction = 0, RULE_formula = 1, RULE_sequence = 2, RULE_listexpr = 3, 
		RULE_expr = 4;
	public static final String[] ruleNames = {
		"deduction", "formula", "sequence", "listexpr", "expr"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "','", "'.'", "'=>'", "'~'", "'&'", "'|'", "'->'", 
		"'<=>'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, "COMMA", "DOT", "LEADSTO", "NOT", "AND", "OR", "IMPLIES", 
		"BICONDITIONAL", "ID", "WS", "ErrorChar"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Wang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public WangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class DeductionContext extends ParserRuleContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public TerminalNode EOF() { return getToken(WangParser.EOF, 0); }
		public DeductionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deduction; }
	}

	public final DeductionContext deduction() throws RecognitionException {
		DeductionContext _localctx = new DeductionContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_deduction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			formula();
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(11);
				match(DOT);
				setState(12);
				formula();
				}
				}
				setState(17);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(18);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormulaContext extends ParserRuleContext {
		public FormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formula; }
	 
		public FormulaContext() { }
		public void copyFrom(FormulaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FormExprContext extends FormulaContext {
		public List<SequenceContext> sequence() {
			return getRuleContexts(SequenceContext.class);
		}
		public SequenceContext sequence(int i) {
			return getRuleContext(SequenceContext.class,i);
		}
		public FormExprContext(FormulaContext ctx) { copyFrom(ctx); }
	}

	public final FormulaContext formula() throws RecognitionException {
		FormulaContext _localctx = new FormulaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_formula);
		int _la;
		try {
			setState(30);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new FormExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(20);
				sequence();
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LEADSTO) {
					{
					setState(21);
					match(LEADSTO);
					setState(22);
					sequence();
					}
				}

				}
				}
				break;
			case 2:
				_localctx = new FormExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				sequence();
				setState(26);
				match(LEADSTO);
				}
				break;
			case 3:
				_localctx = new FormExprContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(28);
				match(LEADSTO);
				setState(29);
				sequence();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SequenceContext extends ParserRuleContext {
		public ListexprContext listexpr() {
			return getRuleContext(ListexprContext.class,0);
		}
		public SequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequence; }
	}

	public final SequenceContext sequence() throws RecognitionException {
		SequenceContext _localctx = new SequenceContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_sequence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << NOT) | (1L << ID))) != 0)) {
				{
				setState(32);
				listexpr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListexprContext extends ParserRuleContext {
		public ListexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listexpr; }
	 
		public ListexprContext() { }
		public void copyFrom(ListexprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SeqExprContext extends ListexprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public SeqExprContext(ListexprContext ctx) { copyFrom(ctx); }
	}

	public final ListexprContext listexpr() throws RecognitionException {
		ListexprContext _localctx = new ListexprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_listexpr);
		int _la;
		try {
			_localctx = new SeqExprContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			expr(0);
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(36);
				match(COMMA);
				setState(37);
				expr(0);
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AndExprContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public AndExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ParensContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParensContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NotExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(WangParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ImplyExprContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ImplyExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class OrExprContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public OrExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class BicondExprContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BicondExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(44);
				match(NOT);
				setState(45);
				expr(7);
				}
				break;
			case ID:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(46);
				match(ID);
				}
				break;
			case T__0:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(47);
				match(T__0);
				setState(48);
				expr(0);
				setState(49);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(67);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(65);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new AndExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(53);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(54);
						((AndExprContext)_localctx).op = match(AND);
						setState(55);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new OrExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(56);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(57);
						((OrExprContext)_localctx).op = match(OR);
						setState(58);
						expr(6);
						}
						break;
					case 3:
						{
						_localctx = new ImplyExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(59);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(60);
						((ImplyExprContext)_localctx).op = match(IMPLIES);
						setState(61);
						expr(4);
						}
						break;
					case 4:
						{
						_localctx = new BicondExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(62);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(63);
						((BicondExprContext)_localctx).op = match(BICONDITIONAL);
						setState(64);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(69);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		case 3:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17I\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\2"+
		"\3\2\3\3\3\3\3\3\5\3\32\n\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\5\4$\n\4"+
		"\3\5\3\5\3\5\7\5)\n\5\f\5\16\5,\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5"+
		"\6\66\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6D\n\6\f\6"+
		"\16\6G\13\6\3\6\2\3\n\7\2\4\6\b\n\2\2\2O\2\f\3\2\2\2\4 \3\2\2\2\6#\3\2"+
		"\2\2\b%\3\2\2\2\n\65\3\2\2\2\f\21\5\4\3\2\r\16\7\6\2\2\16\20\5\4\3\2\17"+
		"\r\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\24\3\2\2\2\23"+
		"\21\3\2\2\2\24\25\7\2\2\3\25\3\3\2\2\2\26\31\5\6\4\2\27\30\7\7\2\2\30"+
		"\32\5\6\4\2\31\27\3\2\2\2\31\32\3\2\2\2\32!\3\2\2\2\33\34\5\6\4\2\34\35"+
		"\7\7\2\2\35!\3\2\2\2\36\37\7\7\2\2\37!\5\6\4\2 \26\3\2\2\2 \33\3\2\2\2"+
		" \36\3\2\2\2!\5\3\2\2\2\"$\5\b\5\2#\"\3\2\2\2#$\3\2\2\2$\7\3\2\2\2%*\5"+
		"\n\6\2&\'\7\5\2\2\')\5\n\6\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+"+
		"\t\3\2\2\2,*\3\2\2\2-.\b\6\1\2./\7\b\2\2/\66\5\n\6\t\60\66\7\r\2\2\61"+
		"\62\7\3\2\2\62\63\5\n\6\2\63\64\7\4\2\2\64\66\3\2\2\2\65-\3\2\2\2\65\60"+
		"\3\2\2\2\65\61\3\2\2\2\66E\3\2\2\2\678\f\b\2\289\7\t\2\29D\5\n\6\t:;\f"+
		"\7\2\2;<\7\n\2\2<D\5\n\6\b=>\f\6\2\2>?\7\13\2\2?D\5\n\6\6@A\f\5\2\2AB"+
		"\7\f\2\2BD\5\n\6\6C\67\3\2\2\2C:\3\2\2\2C=\3\2\2\2C@\3\2\2\2DG\3\2\2\2"+
		"EC\3\2\2\2EF\3\2\2\2F\13\3\2\2\2GE\3\2\2\2\n\21\31 #*\65CE";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}