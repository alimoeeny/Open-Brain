using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.IO;
using System.Web.Script.Serialization;

namespace MyBrain
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public int server_port = 5984;
        public string server_address = @"10.211.55.2";
        public string database_name = @"OpenBrain".ToLower(); //Only lower case charachters are accepted as db name 
        public string[,] DocsList = new string[0,0];

        private void Form1_Load(object sender, EventArgs e)
        {
            HttpWebRequest httpReq = (HttpWebRequest)WebRequest.Create(@"http://" + server_address + @":" + server_port.ToString() + @"/" + database_name);
            httpReq.Method = "GET";
            HttpWebResponse httpResp = (HttpWebResponse)httpReq.GetResponse();
            termMessageOut(httpResp.Headers.ToString());
            StreamReader stred = new StreamReader(httpResp.GetResponseStream());
            string s = stred.ReadToEnd();
            termMessageOut(s);

            UpdateDocsList();
        }
        
        private void UpdateDocsList()
        {
            string s = CouchIt("GET", @"/_design/experiments/_view/allNames");
            JavaScriptSerializer js = new JavaScriptSerializer();
            object jobj = js.DeserializeObject(s);
            System.Collections.Generic.Dictionary<string, object> jobjD = (System.Collections.Generic.Dictionary<string, object>)jobj;
            if (jobjD.Keys.Contains<string>("total_rows"))
            {
                object[] jobjDD = (object[])jobjD["rows"];
                DocsList = new string[jobjDD.Length, 2];
                docsComboBox.Items.Clear();
                //foreach (KeyValuePair<string, object> kvp in (Dictionary<string, object>)jobjDD)
                for(int i = 0; i < jobjDD.Length; i ++)
                {
                    Dictionary<string, object> odic = (Dictionary<string, object>)(((Dictionary<string, object>)jobjDD[i])["value"]);
                    docsComboBox.Items.Add(odic["DocName"].ToString());
                    DocsList[i, 0] = odic["DocId"].ToString();
                    DocsList[i, 1] = odic["DocRev"].ToString();

                    //termMessageOut(((Dictionary<string, object>)jobjDD[i])["value"].ToString());
                    //termMessageOut(kvp.Key + " : " + kvp.Value);
                } 
                ////foreach (string ss in (string[])jobjDD)
                //{
                //    termMessageOut(ss);
                //}
            }
            else
            {
                termMessageOut("What's going on?! are we connected? to the right db?");
            }
        }

        private void termMessageOut(string p)
        {
            terminalTextBox.AppendText(p + "\r\n");
        }

        public string CouchIt(string method, string query)
        {
            if (method == "GET")
            {
                HttpWebRequest httpReq = (HttpWebRequest)WebRequest.Create(@"http://" + server_address + @":" + server_port.ToString() + @"/" + database_name + @"/" + query);
                httpReq.Method = method; // "GET";
                HttpWebResponse httpResp = (HttpWebResponse)httpReq.GetResponse();
                //terminalTextBox.AppendText(httpResp.Headers.ToString());
                StreamReader stred = new StreamReader(httpResp.GetResponseStream());
                string s = stred.ReadToEnd();
                //terminalTextBox.AppendText(s);
                return s;
            }
            else if (method == "POST")
            {
                string postdata = query; // (new UnicodeEncoding()).GetBytes(query);
                HttpWebRequest httpReq = (HttpWebRequest)WebRequest.Create(@"http://" + server_address + @":" + server_port.ToString() + @"/" + database_name);
                httpReq.Method = method;
                httpReq.SendChunked = true;
                //httpReq.TransferEncoding = "utf-8";
                httpReq.MediaType = "text/plain;charset=utf-8"; // "application/json"; // "text/html";
                httpReq.ContentLength = postdata.Length;
                StreamWriter stwrt = new StreamWriter(httpReq.GetRequestStream());
                stwrt.Write(postdata);
                stwrt.Close();
                //ASCIIEncoding encoding=new ASCIIEncoding();
	            //byte[]  data = encoding.GetBytes(postData);
                return "done!";
            }
            else if (method == "PUT")
            {
                string postdata = query; // (new UnicodeEncoding()).GetBytes(query);
                HttpWebRequest httpReq = (HttpWebRequest)WebRequest.Create(@"http://" + server_address + @":" + server_port.ToString() + @"/" + database_name + @"/" + DocsList[docsComboBox.SelectedIndex, 0]);
                httpReq.Method = method;
                httpReq.SendChunked = true;
                //httpReq.TransferEncoding = "utf-8";
                httpReq.MediaType = "text/plain;charset=utf-8"; // "application/json"; // "text/html";
                httpReq.ContentLength = postdata.Length;
                StreamWriter stwrt = new StreamWriter(httpReq.GetRequestStream());
                stwrt.Write(postdata);
                stwrt.Close();
                //ASCIIEncoding encoding=new ASCIIEncoding();
                //byte[]  data = encoding.GetBytes(postData);
                return "done!";
            }
            return "";
        }


        private void button1_Click(object sender, EventArgs e)
        {
            //GetNeuronsList();
        }

        private void GetNeuronsList()
        {
            //HttpWebRequest httpReq = (HttpWebRequest)WebRequest.Create(@"http://" + server_address + @":" + server_port.ToString() + @"/" + database_name + @"/_design/experiments/_view/all");
            //httpReq.Method = "GET";
            //HttpWebResponse httpResp = (HttpWebResponse)httpReq.GetResponse();
            //termMessageOut(httpResp.Headers.ToString());
            //StreamReader stred = new StreamReader(httpResp.GetResponseStream());
            //string s = stred.ReadToEnd();
            //termMessageOut(s);
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (queryTextBox.Text != "")
            {
                termMessageOut(CouchIt("POST", queryTextBox.Text)); 
            }
            else
            {
                termMessageOut("What!?");
            }
        }

        private void docsComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            termMessageOut(DocsList[docsComboBox.SelectedIndex,0]);
            queryTextBox.AppendText(@"{ ""_id': """ + DocsList[docsComboBox.SelectedIndex, 0] + @""",  ""_rev"": """ + DocsList[docsComboBox.SelectedIndex, 1] + "' , } ");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            termMessageOut(CouchIt("PUT", queryTextBox.Text)); 
        }
    }
}
