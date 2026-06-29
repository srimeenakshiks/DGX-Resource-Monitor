"""
Global styles for DGX Monitor.

All CSS is centralized here so the dashboard layout
stays clean and easy to maintain.
"""

CSS = """

/* ============================================================
GENERAL
============================================================ */

.gradio-container{

    width:100% !important;

    max-width:1800px !important;

    margin:0 auto !important;

    padding:25px !important;

    background:#0d1117;

    color:#f0f6fc;

    font-family:Inter,Segoe UI,Arial,sans-serif;
}

/* Remove Gradio padding */

.main{
    padding-top:10px !important;
}


/* ============================================================
HEADER
============================================================ */

.hero{

    background:linear-gradient(
        135deg,
        #161b22,
        #0d1117
    );

    border:1px solid #30363d;

    border-radius:22px;

    padding:35px;

    margin-bottom:25px;

    box-shadow:
        0px 10px 25px rgba(0,0,0,.35);

}

.hero-title{

    font-size:42px;

    font-weight:700;

    color:white;

    margin-bottom:8px;

}

.hero-subtitle{

    color:#8b949e;

    font-size:18px;

}

.hero-status{

    margin-top:18px;

    display:flex;

    gap:14px;

    flex-wrap:wrap;

}

.live-chip{

    background:#238636;

    color:white;

    padding:8px 18px;

    border-radius:999px;

    font-size:14px;

    font-weight:600;

}

.time-chip{

    background:#21262d;

    color:#c9d1d9;

    padding:8px 18px;

    border-radius:999px;

}


/* ============================================================
SECTION TITLES
============================================================ */

.section{

    margin-top:35px;

    margin-bottom:18px;

}

.section h2{

    color:white;

    font-size:30px;

    margin-bottom:5px;

}

.section p{

    color:#8b949e;

}


/* ============================================================
SUMMARY CARDS
============================================================ */

.metric{

    background:#161b22;

    border:1px solid #30363d;

    border-radius:18px;

    padding:22px;

    text-align:center;

    transition:.25s;

    height:150px;

    display:flex;

    flex-direction:column;

    justify-content:center;

}

.metric:hover{

    transform:translateY(-5px);

    box-shadow:

        0 12px 28px rgba(0,0,0,.45);

}

.metric-number{

    font-size:42px;

    font-weight:700;

    color:#58a6ff;

}

.metric-label{

    color:#8b949e;

    font-size:15px;

    margin-top:8px;

}

/* ============================================================
SUMMARY GRID
============================================================ */

.metric-grid{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

    gap:20px;

    margin-bottom:30px;

}


/* ============================================================
GPU CARD
============================================================ */

.gpu-card{

    background:#161b22;
    border:1px solid #30363d;

    border-radius:20px;
    padding:24px;

    display:flex;
    flex-direction:column;

    justify-content:flex-start;

    min-height:350px;

    transition:.25s;

    box-sizing:border-box;
}

.gpu-card:hover{

    transform:translateY(-4px);

    box-shadow:

        0 10px 24px rgba(0,0,0,.40);

}

.gpu-title{

    font-size:22px;

    color:white;

    font-weight:700;

}

.gpu-name{

    color:#8b949e;

    font-size:13px;

    margin-bottom:15px;

}

.gpu-row{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-top:10px;

    min-height:28px;

    font-size:15px;
}

.progress{

    width:100%;

    height:12px;

    background:#21262d;

    border-radius:999px;

    margin-top:10px;

    overflow:hidden;

}

.progress-fill{

    height:100%;

    background:linear-gradient(
        90deg,
        #2ea043,
        #56d364
    );

    transition:width .5s ease;

}

/* ============================================================
GPU GRID
============================================================ */

.gpu-grid{

    display:grid;

    grid-template-columns:repeat(2,minmax(0,1fr));

    gap:24px;

    margin-top:20px;

}

@media (max-width:1100px){

.gpu-grid{

    grid-template-columns:1fr;

}

}


/* ============================================================
TABLES
============================================================ */

table{

    border-radius:15px;

    overflow:hidden;

}


/* ============================================================
FOOTER
============================================================ */

.footer{

    margin-top:45px;

    color:#8b949e;

    text-align:center;

    padding:25px;

    border-top:1px solid #30363d;

}


/* ============================================================
SCROLLBAR
============================================================ */

::-webkit-scrollbar{

    width:12px;

}

::-webkit-scrollbar-thumb{

    background:#30363d;

    border-radius:999px;

}

::-webkit-scrollbar-thumb:hover{

    background:#58a6ff;

}


/* ============================================================
CHARTS
============================================================ */

.plot{

    border-radius:20px;

}


/* ============================================================
RESPONSIVE
============================================================ */

@media (max-width:1200px){

.hero-title{

    font-size:30px;

}

.metric{

    height:130px;

}

.metric-number{

    font-size:34px;

}

}

"""