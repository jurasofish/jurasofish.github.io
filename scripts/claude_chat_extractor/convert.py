#!/usr/bin/env python3
"""
Script to convert a Claude JSON conversation into a markdown document.
"""
from pathlib import Path
import json
from typing import Dict, List, Any, Optional
import re


def process_text_content(content: Dict[str, Any]) -> str:
    """Process text content from the message."""
    assert content["type"] == "text"
    return content["text"] + "\n\n"


def process_tool_use(content: Dict[str, Any]) -> str:
    """Process tool use content from the message."""
    assert content["type"] == "tool_use"
    name = content.get("name", "")
    input_data = content.get("input", {})

    # Format nicely
    formatted_input = json.dumps(input_data, indent=2)

    return f"**Tool Use: {name}**\n\n````json\n{formatted_input}\n````\n\n"


def process_tool_result(content: Dict[str, Any]) -> str:
    """Process tool result content from the message."""
    assert content["type"] == "tool_result"
    name = content.get("name", "")

    result_content = ""
    if "content" in content:
        for item in content["content"]:
            if item.get("type") == "text":
                result_content += item.get("text", "")

    is_error = content.get("is_error", False)

    if is_error:
        return f"**Tool Result (Error): {name}**\n\n````\n{result_content}\n````\n\n"
    else:
        return f"**Tool Result: {name}**\n\n````\n{result_content}\n````\n\n"


def process_message_content(content_list: List[Dict[str, Any]]) -> str:
    """Process all content items in a message."""
    message_text = ""
    for content in content_list:
        content_type = content["type"]

        if content_type == "text":
            message_text += process_text_content(content)
        elif content_type == "tool_use":
            message_text += process_tool_use(content)
        elif content_type == "tool_result":
            message_text += process_tool_result(content)

    return message_text


def clean_markdown(text: str) -> str:
    """Clean up markdown content to avoid rendering issues."""
    # Fix any broken backtick code blocks (ensure they have newlines)
    text = re.sub(r'````(\w+)(?!\n)', r'````\n', text)
    text = re.sub(r'(?<!\n)````', r'\n````', text)

    # Ensure proper spacing around headers
    text = re.sub(r'(?<!\n)(#{1,6} )', r'\n\n\1', text)

    # Remove excessive newlines
    text = re.sub(r'\n{4,}', r'\n\n\n', text)

    # Fix any section markers
    text = re.sub(r'\$0', r'', text)

    return text


def convert_to_markdown(data: Dict[str, Any]) -> str:
    """Convert the JSON conversation data to a markdown document."""
    conversation_title = data.get("name", "Conversation")
    markdown = f"# {conversation_title}\n\n"

    chat_messages = data.get("chat_messages", [])

    for message in chat_messages:
        sender = message.get("sender", "unknown")
        content_list = []

        if "content" in message:
            content_list = message["content"]

        message_content = process_message_content(content_list)

        if sender == "human":
            markdown += f"## Human\n\n{message_content}\n\n"
        else:
            markdown += f"## Assistant\n\n{message_content}\n\n"

    return markdown
    # return clean_markdown(markdown)


def main() -> None:
    data_path = Path(__file__).parent / "data.json"
    output_path = Path(__file__).parent / "conversation.md"

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        markdown = convert_to_markdown(data)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"Successfully converted to markdown: {output_path}")

    except json.JSONDecodeError:
        print(f"Error: The file at {data_path} is not valid JSON")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()