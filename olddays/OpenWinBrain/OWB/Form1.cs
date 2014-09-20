using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data;
using Npgsql;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            NpgsqlConnectionStringBuilder pgsCS = new NpgsqlConnectionStringBuilder();
            pgsCS.Host = @"10.211.55.2";
            pgsCS.Database = @"openbrain";
            pgsCS.UserName = @"postgres";
            pgsCS.Password = @"postgres";
            NpgsqlConnection pgCon = new NpgsqlConnection(pgsCS.ConnectionString);
            pgCon.Open();
            pgCon.Close();
        }
    }
}
