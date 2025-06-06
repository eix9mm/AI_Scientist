#!/usr/bin/env python3
"""
AI Scientist Documentation Verification Script
このスクリプトは、ドキュメンテーションが適切に設置されているかを確認します。
"""

import os
import sys

def check_documentation():
    """ドキュメンテーションの存在と内容を確認"""
    docs_dir = "docs"
    required_files = [
        "実装解説書.md",
        "DEVELOPER_GUIDE.md", 
        "README.md"
    ]
    
    print("🔍 AI Scientist ドキュメンテーション確認中...")
    
    # docs ディレクトリの存在確認
    if not os.path.exists(docs_dir):
        print("❌ docs ディレクトリが見つかりません")
        return False
    
    # 必要なファイルの存在確認
    missing_files = []
    for file in required_files:
        file_path = os.path.join(docs_dir, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
        else:
            # ファイルサイズ確認
            size = os.path.getsize(file_path)
            print(f"✅ {file} - {size:,} bytes")
    
    if missing_files:
        print("❌ 以下のファイルが見つかりません:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ 全てのドキュメンテーションファイルが正常に確認されました")
    
    # 基本的な内容確認
    print("\n📋 ドキュメント内容の基本確認:")
    
    # 実装解説書の内容確認
    impl_doc_path = os.path.join(docs_dir, "実装解説書.md")
    with open(impl_doc_path, 'r', encoding='utf-8') as f:
        impl_content = f.read()
        if "システム全体のアーキテクチャ" in impl_content:
            print("✅ 実装解説書にアーキテクチャ説明が含まれています")
        if "テンプレートシステム" in impl_content:
            print("✅ 実装解説書にテンプレートシステム説明が含まれています")
    
    # 開発者ガイドの内容確認
    dev_guide_path = os.path.join(docs_dir, "DEVELOPER_GUIDE.md")
    with open(dev_guide_path, 'r', encoding='utf-8') as f:
        dev_content = f.read()
        if "Code Architecture" in dev_content:
            print("✅ 開発者ガイドにコードアーキテクチャ説明が含まれています")
        if "Security Considerations" in dev_content:
            print("✅ 開発者ガイドにセキュリティ考慮事項が含まれています")
    
    print("\n🎉 ドキュメンテーション確認完了!")
    return True

def main():
    """メイン実行関数"""
    print("=" * 60)
    print("AI Scientist Repository Documentation Verification")
    print("=" * 60)
    
    if check_documentation():
        print("\n✅ 全ての確認が完了しました。ドキュメンテーションは正常に設置されています。")
        print("\n📚 利用方法:")
        print("   - 初心者: docs/実装解説書.md から開始")
        print("   - 開発者: docs/DEVELOPER_GUIDE.md を参照")
        print("   - 概要: docs/README.md を確認")
        return 0
    else:
        print("\n❌ ドキュメンテーションに問題があります。上記のエラーを確認してください。")
        return 1

if __name__ == "__main__":
    sys.exit(main())