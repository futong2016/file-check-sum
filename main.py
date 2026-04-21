import hashlib
import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileChecksumTool:
    def __init__(self, root):
        self.root = root
        self.root.title("文件内容校验工具")
        self.root.geometry("600x400")
        
        # 状态变量
        self.file_path = tk.StringVar()
        self.algorithm = tk.StringVar(value="SHA-256")
        self.result_hash = tk.StringVar()
        self.expected_hash = tk.StringVar()
        self.status_text = tk.StringVar(value="就绪")
        
        self.setup_ui()

    def calculate_file_hash(self, file_path, algorithm):
        """计算文件的哈希值，支持大文件分块读取"""
        hash_func = getattr(hashlib, algorithm.lower().replace("-", ""))()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except Exception as e:
            return f"错误: {str(e)}"

    def compare_hashes(self):
        """对比计算结果与预期哈希值"""
        calc = self.result_hash.get().strip().lower()
        exp = self.expected_hash.get().strip().lower()
        
        if not calc or not exp:
            return None
        return calc == exp

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 文件选择
        file_frame = ttk.LabelFrame(main_frame, text="文件选择", padding="10")
        file_frame.pack(fill=tk.X, pady=5)
        
        ttk.Entry(file_frame, textvariable=self.file_path, width=50).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        ttk.Button(file_frame, text="浏览...", command=self.browse_file).pack(side=tk.LEFT, padx=5)

        # 算法和操作
        opt_frame = ttk.Frame(main_frame, padding="5")
        opt_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(opt_frame, text="选择算法:").pack(side=tk.LEFT, padx=5)
        algo_combo = ttk.Combobox(opt_frame, textvariable=self.algorithm, values=["MD5", "SHA-1", "SHA-256"], state="readonly", width=10)
        algo_combo.pack(side=tk.LEFT, padx=5)
        
        self.calc_btn = ttk.Button(opt_frame, text="开始计算", command=self.start_calculation)
        self.calc_btn.pack(side=tk.RIGHT, padx=5)

        # 结果显示
        res_frame = ttk.LabelFrame(main_frame, text="计算结果", padding="10")
        res_frame.pack(fill=tk.X, pady=5)
        
        ttk.Entry(res_frame, textvariable=self.result_hash, state="readonly").pack(fill=tk.X, padx=5, pady=5)

        # 预期比对
        comp_frame = ttk.LabelFrame(main_frame, text="哈希比对 (预期值)", padding="10")
        comp_frame.pack(fill=tk.X, pady=5)
        
        self.exp_entry = ttk.Entry(comp_frame, textvariable=self.expected_hash)
        self.exp_entry.pack(fill=tk.X, padx=5, pady=5)
        self.exp_entry.bind("<KeyRelease>", lambda e: self.update_comparison())
        
        self.comp_label = ttk.Label(comp_frame, text="", font=("Arial", 10, "bold"))
        self.comp_label.pack(pady=5)

        # 状态栏
        status_bar = ttk.Label(self.root, textvariable=self.status_text, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_path.set(filename)
            self.result_hash.set("")
            self.update_comparison()

    def start_calculation(self):
        file_p = self.file_path.get()
        algo = self.algorithm.get()
        
        if not file_p or not os.path.exists(file_p):
            messagebox.showerror("错误", "请选择有效的文件")
            return
            
        self.calc_btn.config(state=tk.DISABLED)
        self.status_text.set(f"正在计算 {algo}...")
        self.result_hash.set("")
        self.update_comparison()
        
        # 在新线程中运行计算
        thread = threading.Thread(target=self._run_calculation, args=(file_p, algo))
        thread.daemon = True
        thread.start()

    def _run_calculation(self, file_p, algo):
        res = self.calculate_file_hash(file_p, algo)
        
        # 回到主线程更新 UI
        self.root.after(0, self._finish_calculation, res)

    def _finish_calculation(self, res):
        self.result_hash.set(res)
        self.calc_btn.config(state=tk.NORMAL)
        self.status_text.set("计算完成")
        self.update_comparison()

    def update_comparison(self):
        res = self.compare_hashes()
        if res is True:
            self.comp_label.config(text="匹配", foreground="green")
        elif res is False:
            self.comp_label.config(text="不匹配", foreground="red")
        else:
            self.comp_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileChecksumTool(root)
    root.mainloop()
