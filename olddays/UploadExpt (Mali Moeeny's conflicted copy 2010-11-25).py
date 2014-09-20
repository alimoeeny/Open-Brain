import httplib
import json
import base64
import string
from numpy import squeeze

server = '10.1.1.199';
userid = 'openbrain';
upss = 'alimoeen';
db = 'openbrain';
auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + upss))

def Uploadit(Expt):
    if not Expt.dataLoaded:
        if Expt.name[0:2]=='dae':
            Expt.loadData('/Users/ali/Dropbox/Projects/Open-Brain/data/dae/' + Expt.name[3:6] + '/' + Expt.name);
        else:
            Expt.loadData('/Users/ali/Dropbox/Projects/Open-Brain/data/icarus/' + Expt.name[2:5] + '/' + Expt.name);

    ExptFields = dir(Expt);

    #hdb = httplib.HTTPConnection('openbrain.cloudant.com', 5984, timeout=30);
    hdb = httplib.HTTPConnection(server, 5984, timeout=30);
    hdb.connect();
    if server=='10.1.1.199':
        hdb.request('GET',''.join('/'+db+'/_design/experiments/_view/by_name?key="' + Expt.name +'"'));
    else:
        hdb.request('GET',''.join('/'+db+'/_design/experiments/_view/by_name?key="' + Expt.name +'"'), [], {'Authorization': auth});
    r1 = hdb.getresponse();
    data = json.loads(r1.read());

    
    details = {};
    if data['rows']<>[]:
        if data['rows'][0]['id'] <> '':
            details['_id'] = data['rows'][0]['id'];
            details['_rev'] = data['rows'][0]['value']['_rev']

    details['name']  = Expt.name;


    if 'Area' in ExptFields:
        try:
            details['Area'] = Expt.Area.item().item().item()
        except:
            sa = '';
            for aic in range(0,Expt.Area.item().size):
                sa += Expt.Area.item()[0][aic][0];
                
    details['Bc'] = Expt.Bc[0][0]
    details['Bh'] = Expt.Bh[0][0]
    details['BlockStart'] = Expt.BlockStart[0][0]
    details['BlockedStim'] = Expt.BlockedStim[0][0]
    if 'Br' in ExptFields:
        details['Br'] = Expt.Br[0][0]
    details['Bs'] = Expt.Bs.item().item()
    details['Bt'] = Expt.Bt[0][0]
    details['Bw'] = Expt.Bw[0][0]
    if 'Ca' in ExptFields:
        details['Ca'] = Expt.Ca.item().item()
    #details['Cluster'] = Expt.Cluster.item().item()
    #details['Clusters'] = Expt.Clusters.item()
    #details['CombineDate'] = Expt.CombineDate[0][0]
    #details['Combined'] = Expt.Combined[0]
    #details['Combineids'] = Expt.Combineids[0].__str__()
    if 'CorLoop' in ExptFields:
        details['CorLoop'] = Expt.CorLoop[0][0]
    details['Dc'] = Expt.Dc[0][0]
    details['Dm'] = Expt.Dm[0][0]
    details['Dw'] = Expt.Dw[0][0]
    if 'End' in ExptFields:
        details['End'] = Expt.End[0][0]
    details['Er'] = Expt.Er[0][0]
    if 'Ex' in ExptFields:
        details['Ex'] = 'Ex' + Expt.Ex.item().item()
    details['Fa'] = Expt.Fa[0][0]
    details['FalseStart'] = Expt.FalseStart[0][0]
    details['Fr'] = Expt.Fr[0][0]
    details['Fs'] = Expt.Fs[0][0]
    if 'IB' in ExptFields:
        details['IB'] = Expt.IB[0][0]
    details['IS'] = Expt.IS[0][0]
    details['Id'] = Expt.Id[0][0]
    if 'Im' in ExptFields:
        details['Im'] = Expt.Im[0][0]
    details['Nf'] = Expt.Nf[0][0]
    details['O2'] = Expt.O2[0][0]
    details['OR'] = Expt.OR[0][0]
    if 'Op' in ExptFields:
        details['Op'] = Expt.Op[0][0]
    if 'Options' in ExptFields: 
        if Expt.Options.tolist().size > 0:
            details['Options'] = Expt.Options.item().item()
    details['Pd'] = Expt.Pd[0][0]
    #details['Peninfo'] = Expt.Peninfo.item()
    if 'Pp' in ExptFields:
        details['Pp'] = Expt.Pp[0][0]
    details['RespDir'] = Expt.RespDir[0][0]
    details['Ri'] = Expt.Ri[0][0]
    details['Ro'] = Expt.Ro[0][0]
    if 'Rx' in ExptFields:
        details['Rx'] = Expt.Rx[0][0]
    if 'Ry' in ExptFields:
        details['Ry'] = Expt.Ry[0][0]
    details['Sa'] = Expt.Sa[0][0]
    details['Spike2Version'] = Expt.Spike2Version[0][0]
    details['Spikelist'] = Expt.Spikelist[0][0]
    #details['SpkStats'] = Expt.SpkStats.item()
    details['Sr'] = Expt.Sr[0][0]
    details['St'] = Expt.St[0][0]
    if 'Start' in ExptFields:
        details['Start'] = Expt.Start[0][0]
    if 'StartDepth' in ExptFields:
        details['StartDepth'] = Expt.StartDepth[0][0]
    details['Startev'] = Expt.Startev[0][0]
    details['Trial'] = Expt.Trial[0][0]
    details['Trials'] = {};
    tc = 0;
    TrialFields = dir(Expt.Trials[0]);
    for tt in Expt.Trials:
        tcs = {};
        for tf in TrialFields:
            if not tf in ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__hash__', '__init__', '__module__', '__new__', '__reduce_ex__', '__rep__', '__setattr__', '__subclasshook__', '__weakref__', '__str__','__getattribute__', '__reduce__', '__sizeof__', '__repr__', 'Ocodes', ]:
                if tf in ['End',]:
                    tcs[tf] = eval('tt.' + tf );
                elif tf in ['OptionCode']:
                    tcs[tf] = eval('tt.' + tf + '.item()')
                elif tf in ['Events', 'fh', 'fi', 'fp', ]:
                    try:
                        tmpjsontest = json.dumps(eval('tt.' + tf + '.item()')) 
                        tcs[tf] = eval('tt.' + tf + '.item()')
                    except:
                        try:
                            tmpjson = json.dumps(eval('tt.' + tf + '[0][0]'))
                            tcs[tf] = eval('tt.' + tf + '[0][0]')
                        except:
                            try:
                                tmpjson = json.dumps(eval('tt.' + tf + '.__str__()'))
                                tcs[tf] = eval('tt.' + tf + '.__str__()')
                            except:
                                print 'Cannot do this! ' + eval('tt.' + tf + '.__str__()')
                elif tf in ['Spikes', 'OSpikes', ]:
                    try:
                        try:
                            tcs[tf] = int(squeeze([eval('tt.' + tf)]));
                        except Exception as inst:
                            if(eval('tt.'+tf)!=[]):
                                tempintList= [];
                                ttlen = eval('tt.' + tf + '.__len__()');
                                for tii in range(0, ttlen):
                                    tempintList.append(int(eval('tt.'+tf +'['+tii.__str__()+']')));
                                tcs[tf] = tempintList;
                    except Exception as inst:
                        print("Cannot do the "+ tf + "!");
                        print(inst);
                        print(eval('tt.'+tf));
                else:
                    tcs[tf] = eval('tt.' + tf );
            
                    
        details['Trials'][tc] = tcs;
        tc = tc + 1;

    #print details['Trials']
    details['TrueEnd'] = Expt.TrueEnd[0][0]
    if 'Tu' in ExptFields:
        details['Tu'] = Expt.Tu.item().item()
    if 'Vs' in ExptFields:
        details['Vs'] = Expt.Vs[0][0]
    if 'Wr' in ExptFields:
        details['Wr'] = Expt.Wr.item().item()
    details['a2'] = Expt.a2[0][0]
    if 'ap' in ExptFields:
        details['ap'] = Expt.ap[0][0]
    details['bc'] = Expt.bc[0][0]
    details['bd'] = Expt.bd[0][0]
    details['bh'] = Expt.bh[0][0]
    details['bi'] = Expt.bi[0][0]
    details['bo'] = Expt.bo[0][0]
    if 'bstimes' in ExptFields:
        details['bstimes'] = Expt.bstimes[0][0]
    details['bw'] = Expt.bw[0][0]
    if 'bz' in ExptFields:
        details['bz'] = Expt.bz[0][0]
    details['c2'] = Expt.c2[0][0]
    details['cb'] = Expt.cb[0][0]
    details['ce'] = Expt.ce[0][0]
    details['ch'] = Expt.ch[0][0]
    details['cj'] = Expt.cj[0][0]
    if 'clist' in ExptFields:
        details['clist'] = Expt.clist[0][0]
    details['cm'] = Expt.cm.item().item()
    details['co'] = Expt.co[0][0]
    details['cs'] = Expt.cs[0][0]
    if 'cx' in ExptFields:
        try:
            details['cx'] = Expt.cx[0][0]
        except:
            try:
                details['cx'] = Expt.cx.item().item()
            except:
                print 'No cx here!'
    details['dd'] = Expt.dd[0][0]
    details['delay'] = Expt.delay[0][0]
    details['depths'] = Expt.depths[0][0]
    if 'dfx' in ExptFields:
        details['dfx'] = Expt.dfx[0][0]
    if 'dfy' in ExptFields:
        details['dfy'] = Expt.dfy[0][0]
    details['dg'] = Expt.dg[0][0]
    details['dm'] = Expt.dm[0][0]
    details['dp'] = Expt.dp[0][0]
    details['dq'] = Expt.dq[0][0]
    details['dr'] = Expt.dr[0][0]
    details['ds'] = Expt.ds[0][0]
    details['dt'] = Expt.dt[0][0]
    details['du'] = Expt.du[0][0]
    details['dw'] = Expt.dw[0][0]
    details['dx'] = Expt.dx[0][0]
    details['dy'] = Expt.dy[0][0]
    details['e2'] = Expt.e2.item().item()
    details['e3'] = Expt.e3.item().item()
    details['ed'] = Expt.ed[0][0]
    details['ei'] = Expt.ei[0][0]
    details['em'] = Expt.em[0][0]
    details['et'] = Expt.et.item().item()
    details['experimentType'] = Expt.experimentType
    details['expname'] = Expt.expname.item().item()
    details['f2'] = Expt.f2[0][0]
    details['fH'] = Expt.fH[0][0]
    details['fc'] = Expt.fc[0][0]
    details['fd'] = Expt.fd[0][0]
    try:
        tmpjfh = json.dumps(Expt.fh[0][0]);
        details['fh'] = Expt.fh[0][0];
    except:
        pass
    details['fi'] = Expt.fi[0][0]
    details['fn'] = Expt.fn[0][0]
    details['fr'] = Expt.fr[0][0]
    if 'frameperiod' in ExptFields:
        details['frameperiod'] = Expt.frameperiod[0][0]
    details['fs'] = Expt.fs[0][0]
    details['fw'] = Expt.fw[0][0]
    details['fx'] = Expt.fx[0][0]
    details['fy'] = Expt.fy[0][0]
    details['fz'] = Expt.fz[0][0]
    details['hd'] = Expt.hd[0][0]
    details['hi'] = Expt.hi[0][0]
    if 'hx' in ExptFields:
        details['hx'] = Expt.hx[0][0]
    details['i2'] = Expt.i2[0][0]
    details['i3'] = Expt.i3[0][0]
    details['ic'] = Expt.ic[0][0]
    details['id'] = Expt.id[0][0]
    details['ip'] = Expt.ip[0][0]
    details['jc'] = Expt.jc[0][0]
    details['jl'] = Expt.jl[0][0]
    details['jn'] = Expt.jn[0][0]
    details['js'] = Expt.js[0][0]
    details['jt'] = Expt.jt[0][0]
    details['jv'] = Expt.jv[0][0]
    details['jx'] = Expt.jx[0][0]
    details['lb'] = Expt.lb[0][0]
    details['m2'] = Expt.m2[0][0]
    details['mD'] = Expt.mD[0][0]
    details['me'] = Expt.me[0][0]
    details['mf'] = Expt.mf[0][0]
    details['mo'] = Expt.mo[0][0]
    details['monkeyName'] = Expt.monkeyName
    if 'mt' in ExptFields:
        if Expt.mt <> []:
            details['mt'] = Expt.mt.item().item()
    details['n2'] = Expt.n2[0][0]
    details['n3'] = Expt.n3[0][0]
    details['nc'] = Expt.nc[0][0]
    details['nf'] = Expt.nf[0][0]
    details['np'] = Expt.np[0][0]
    details['nr'] = Expt.nr[0][0]
    details['nspk'] = Expt.nspk[0][0]
    details['nt'] = Expt.nt[0][0]
    details['nx'] = Expt.nx[0][0]
    details['o2'] = Expt.o2[0][0]
    details['ob'] = Expt.ob[0][0]
    details['od'] = Expt.od[0][0]
    details['p2'] = Expt.p2[0][0]
    details['pd'] = Expt.pd[0][0]
    details['ph'] = Expt.ph[0][0]
    details['pi'] = Expt.pi[0][0]
    details['po'] = Expt.po[0][0]
    details['pr'] = Expt.pr[0][0]
    details['psych'] = Expt.psych[0][0]
    details['pw'] = Expt.pw[0][0]
    details['px'] = Expt.px[0][0]
    details['py'] = Expt.py[0][0]
    if 'rOp' in ExptFields:
        details['rOp'] = Expt.rOp[0][0]
    if 'rPp' in ExptFields:
        details['rPp'] = Expt.rPp[0][0]
    details['ra'] = Expt.ra[0][0]
    details['rc'] = Expt.rc[0][0]
    details['rf'] = Expt.rf[0][0]
    if 'rfstr' in ExptFields:
        details['rfstr'] = Expt.rfstr.item().item()
    details['rk'] = Expt.rk[0][0]
    details['rp'] = Expt.rp[0][0]
    if 'rr' in ExptFields:
        details['rr'] = Expt.rr[0][0]
    details['rw'] = Expt.rw[0][0]
    details['rwdir'] = Expt.rwdir[0][0]
    details['s0'] = Expt.s0[0][0]
    details['sM'] = Expt.sM[0][0]
    details['sP'] = Expt.sP[0][0]
    details['sb'] = Expt.sb.item().item()
    details['sd'] = Expt.sd[0][0]
    details['se'] = Expt.se[0][0]
    details['serdelay'] = Expt.serdelay[0][0]
    details['sf'] = Expt.sf[0][0]
    details['sh'] = Expt.sh[0][0]
    details['sl'] = Expt.sl[0][0]
    details['sm'] = Expt.sm[0][0]
    details['so'] = Expt.so[0][0]
    details['sp'] = Expt.sp[0][0]
    details['sq'] = Expt.sq[0][0]
    details['ss'] = Expt.ss[0][0]
    details['st'] = Expt.st[0][0]
    details['stored'] = Expt.stored[0][0]
    details['sv'] = Expt.sv[0][0]
    details['sx'] = Expt.sx[0][0]
    details['sy'] = Expt.sy[0][0]
    details['t2'] = Expt.t2[0][0]
    details['ta'] = Expt.ta[0][0]
    details['tf'] = Expt.tf[0][0]
    details['ti'] = Expt.ti[0][0]
    details['tl'] = Expt.tl[0][0]
    details['to'] = Expt.to[0][0]
    details['trange'] = Expt.trange[0][0]
    if 'uf' in ExptFields:
        if Expt.uf.tolist().size > 0:
            details['uf'] = Expt.uf.item().item()
    details['unstored'] = Expt.unstored[0][0]
    details['vc'] = Expt.vc[0][0]
    details['vd'] = Expt.vd[0][0]
    details['ve'] = Expt.ve[0][0]
    details['vh'] = Expt.vh.item().item()
    details['vm'] = Expt.vm[0][0]
    details['vr'] = Expt.vr.item().item()
    details['vs'] = Expt.vs[0][0]
    details['vv'] = Expt.vv[0][0]
    details['vw'] = Expt.vw[0][0]
    details['wd'] = Expt.wd[0][0]
    details['wf'] = Expt.wf[0][0]
    details['wi'] = Expt.wi[0][0]
    details['wr'] = Expt.wr[0][0]
    details['x1t'] = Expt.x1t[0][0]
    details['x2t'] = Expt.x2t[0][0]
    details['x3t'] = Expt.x3t[0][0]
    details['x4t'] = Expt.x4t[0][0]
    details['xd'] = Expt.xd[0][0]
    details['xn'] = Expt.xn[0][0]
    details['xo'] = Expt.xo[0][0]
    details['yn'] = Expt.yn[0][0]
    details['yo'] = Expt.yo[0][0]
    details['zf'] = Expt.zf[0][0]
    details['zx'] = Expt.zx[0][0]





    hdb = httplib.HTTPConnection(server, 5984, timeout=30);
    #hdb = httplib.HTTPConnection('openbrain.cloudant.com', 5984, timeout=30);
    hdb.connect();
    if server=='10.1.1.199':
        hdb.request('POST',''.join('/'+db), json.dumps(details));
    else:
        hdb.request('POST',''.join('/'+db), json.dumps(details), {'Authorization': auth});
    r1 = hdb.getresponse();
    dbdoc = json.loads(r1.read());
    
